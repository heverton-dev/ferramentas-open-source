#!/usr/bin/env node
/**
 * StateManager — Gerenciador de Estado da Esteira com SQLite
 *
 * Rastreia tentativas de fases, status e histórico de execuções.
 * Cria DB e tabelas automaticamente na primeira execução.
 *
 * Uso:
 *   import { StateManager } from './state-manager.js';
 *   const sm = new StateManager();
 *   sm.recordPhaseAttempt('run-001', 'phase-1', 1, 95, [], 'success');
 *   const status = sm.getPhaseStatus('run-001', 'phase-1');
 */

import Database from 'better-sqlite3';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const DB_PATH = path.join(__dirname, '..', 'estado_esteira.db');

export class StateManager {
  constructor() {
    this.db = new Database(DB_PATH);
    this.db.pragma('journal_mode = WAL');
    this._initializeTables();
  }

  /**
   * Inicializa as tabelas se não existirem.
   * @private
   */
  _initializeTables() {
    // Tabela de tentativas: histórico completo de cada tentativa
    this.db.exec(`
      CREATE TABLE IF NOT EXISTS phase_attempts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        runId TEXT NOT NULL,
        phaseId TEXT NOT NULL,
        attempt INTEGER NOT NULL,
        score REAL NOT NULL,
        gaps TEXT,
        result TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        UNIQUE(runId, phaseId, attempt)
      );
      CREATE INDEX IF NOT EXISTS idx_run_phase ON phase_attempts(runId, phaseId);
      CREATE INDEX IF NOT EXISTS idx_run ON phase_attempts(runId);
    `);

    // Tabela de status: resumo atual de cada fase por execução
    this.db.exec(`
      CREATE TABLE IF NOT EXISTS phase_status (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        runId TEXT NOT NULL,
        phaseId TEXT NOT NULL,
        lastAttempt INTEGER NOT NULL,
        lastScore REAL NOT NULL,
        status TEXT NOT NULL,
        updatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,
        UNIQUE(runId, phaseId)
      );
      CREATE INDEX IF NOT EXISTS idx_status_run ON phase_status(runId);
    `);
  }

  /**
   * Registra uma tentativa de fase com score, gaps e resultado.
   * @param {string} runId - ID da execução
   * @param {string} phaseId - ID da fase
   * @param {number} attempt - Número da tentativa (1, 2, 3...)
   * @param {number} score - Score obtido (0-100)
   * @param {Array} gaps - Array de gaps/problemas encontrados
   * @param {string} result - Resultado ('success', 'partial', 'failed')
   */
  recordPhaseAttempt(runId, phaseId, attempt, score, gaps = [], result = 'pending') {
    const gapsJson = JSON.stringify(gaps);
    const status = score >= 90 ? 'success' : score >= 70 ? 'partial' : 'failed';

    try {
      // Inserir tentativa no histórico
      const insert = this.db.prepare(`
        INSERT INTO phase_attempts (runId, phaseId, attempt, score, gaps, result)
        VALUES (?, ?, ?, ?, ?, ?)
      `);
      insert.run(runId, phaseId, attempt, score, gapsJson, result);

      // Atualizar ou inserir status
      const upsert = this.db.prepare(`
        INSERT INTO phase_status (runId, phaseId, lastAttempt, lastScore, status, updatedAt)
        VALUES (?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
        ON CONFLICT(runId, phaseId)
        DO UPDATE SET
          lastAttempt = excluded.lastAttempt,
          lastScore = excluded.lastScore,
          status = excluded.status,
          updatedAt = CURRENT_TIMESTAMP
      `);
      upsert.run(runId, phaseId, attempt, score, status);

      return { ok: true, attempt, score, status };
    } catch (err) {
      console.error(`Erro ao registrar tentativa: ${err.message}`);
      throw err;
    }
  }

  /**
   * Obtém o status atual de uma fase.
   * @param {string} runId - ID da execução
   * @param {string} phaseId - ID da fase
   * @returns {Object|null} Status com lastAttempt, lastScore, status ou null
   */
  getPhaseStatus(runId, phaseId) {
    const row = this.db.prepare(`
      SELECT lastAttempt, lastScore, status, updatedAt
      FROM phase_status
      WHERE runId = ? AND phaseId = ?
    `).get(runId, phaseId);

    return row || null;
  }

  /**
   * Obtém o histórico completo de tentativas de uma fase.
   * @param {string} runId - ID da execução
   * @param {string} phaseId - ID da fase
   * @returns {Array} Array de tentativas
   */
  getPhaseHistory(runId, phaseId) {
    const rows = this.db.prepare(`
      SELECT attempt, score, gaps, result, timestamp
      FROM phase_attempts
      WHERE runId = ? AND phaseId = ?
      ORDER BY attempt ASC
    `).all(runId, phaseId);

    return rows.map(row => ({
      ...row,
      gaps: JSON.parse(row.gaps || '[]')
    }));
  }

  /**
   * Obtém todas as execuções (runIds).
   * @returns {Array} Array de runIds ordenados por timestamp
   */
  getAllRuns() {
    const rows = this.db.prepare(`
      SELECT runId, MAX(timestamp) as latest
      FROM phase_attempts
      GROUP BY runId
      ORDER BY latest DESC
    `).all();

    return rows.map(r => r.runId);
  }

  /**
   * Obtém um resumo completo de uma execução.
   * @param {string} runId - ID da execução
   * @returns {Object} Objeto com phases, stats e timeline
   */
  getRunSummary(runId) {
    const phases = this.db.prepare(`
      SELECT phaseId, lastAttempt, lastScore, status
      FROM phase_status
      WHERE runId = ?
      ORDER BY phaseId
    `).all(runId);

    const totalAttempts = this.db.prepare(`
      SELECT COUNT(*) as count FROM phase_attempts WHERE runId = ?
    `).get(runId).count;

    const avgScore = this.db.prepare(`
      SELECT AVG(lastScore) as avg FROM phase_status WHERE runId = ?
    `).get(runId).avg || 0;

    const successCount = phases.filter(p => p.status === 'success').length;

    const timeline = this.db.prepare(`
      SELECT phaseId, attempt, score, result, timestamp
      FROM phase_attempts
      WHERE runId = ?
      ORDER BY timestamp ASC
    `).all(runId);

    return {
      runId,
      phaseCount: phases.length,
      phases,
      stats: {
        totalAttempts,
        averageScore: Math.round(avgScore * 100) / 100,
        successfulPhases: successCount,
        successRate: Math.round((successCount / phases.length) * 100) || 0
      },
      timeline
    };
  }

  /**
   * Limpa dados antigos (mais de X dias).
   * @param {number} daysOld - Remover dados com mais de N dias
   * @returns {Object} Resultado da limpeza
   */
  cleanOldData(daysOld = 30) {
    const result = this.db.prepare(`
      DELETE FROM phase_attempts
      WHERE timestamp < datetime('now', '-' || ? || ' days')
    `).run(daysOld);

    this.db.prepare(`
      DELETE FROM phase_status
      WHERE updatedAt < datetime('now', '-' || ? || ' days')
    `).run(daysOld);

    return {
      removed: result.changes,
      daysOld
    };
  }

  /**
   * Exporta dados em JSON.
   * @param {string} runId - ID da execução (opcional, se omitido exporta tudo)
   * @returns {Object} Dados em formato JSON
   */
  exportData(runId = null) {
    const attempts = runId
      ? this.db.prepare('SELECT * FROM phase_attempts WHERE runId = ?').all(runId)
      : this.db.prepare('SELECT * FROM phase_attempts').all();

    const status = runId
      ? this.db.prepare('SELECT * FROM phase_status WHERE runId = ?').all(runId)
      : this.db.prepare('SELECT * FROM phase_status').all();

    return {
      attempts: attempts.map(a => ({
        ...a,
        gaps: JSON.parse(a.gaps || '[]')
      })),
      status,
      exportedAt: new Date().toISOString()
    };
  }

  /**
   * Fecha a conexão com o banco de dados.
   */
  close() {
    this.db.close();
  }
}

export default StateManager;
