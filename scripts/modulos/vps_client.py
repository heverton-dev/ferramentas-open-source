# -*- coding: utf-8 -*-
import os
import re
import requests

# Validacao de certificado LIGADA por padrao: a senha de administrador e o JWT do
# Portainer trafegam nestas chamadas. Sem verificacao, um intermediario na rota se
# passa pelo painel e captura a credencial.
#
# Valvula de escape para VPS com certificado autoassinado: exporte
# PORTAINER_TLS_INSECURE=1. A excecao continua possivel, mas deixa de ser silenciosa.
VERIFICAR_TLS = os.environ.get("PORTAINER_TLS_INSECURE", "").strip() not in ("1", "true", "True")

if not VERIFICAR_TLS:
    import urllib3
    urllib3.disable_warnings()
    import sys as _sys
    print("[AVISO] PORTAINER_TLS_INSECURE=1: certificado NAO sera validado. "
          "A senha do Portainer trafega sem garantia de destino.", file=_sys.stderr)

class PortainerClient:
    def __init__(self, env_path=None):
        if env_path is None:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            root_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
            env_path = os.path.join(root_dir, '.env')
            if not os.path.exists(env_path):
                env_path = os.path.join(os.getcwd(), '.env')

        self.env_path = env_path
        self.url = None
        self.username = None
        self.password = None
        self.jwt = None
        self.endpoint_id = 1
        self._load_env()

    def _clean_val(self, val):
        val = val.strip()
        if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
            val = val[1:-1]
        return val.strip()

    def _load_env(self):
        if not os.path.exists(self.env_path):
            raise FileNotFoundError(f'Arquivo .env nao encontrado em: {self.env_path}')

        with open(self.env_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                if 'PORTAINER_URL' in line.upper() or 'PORTEINER_URL' in line.upper():
                    val = self._clean_val(line.split('=', 1)[1])
                    val = re.sub(r'/#!.*', '', val).rstrip('/')
                    self.url = val
                elif 'PORTAINER_USERNAME' in line.upper() or 'PORTEINER_USERNAME' in line.upper():
                    self.username = self._clean_val(line.split('=', 1)[1])
                elif 'PORTAINER_PASSWORD' in line.upper() or 'PORTEINER_PASSWORD' in line.upper():
                    self.password = self._clean_val(line.split('=', 1)[1])

        # Gate de credenciais (scripts/validar_env.py): recusa variavel ausente, vazia
        # ou ainda com valor de exemplo, e lista TODOS os problemas de uma vez — corrigir
        # um por execucao transforma configuracao em tentativa e erro.
        try:
            import sys as _sys
            _scripts = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            if _scripts not in _sys.path:
                _sys.path.insert(0, _scripts)
            from validar_env import exigir as _exigir
            _exigir('PORTAINER_URL', 'PORTAINER_USERNAME', 'PORTAINER_PASSWORD',
                    env={'PORTAINER_URL': self.url or '',
                         'PORTAINER_USERNAME': self.username or '',
                         'PORTAINER_PASSWORD': self.password or ''})
        except ImportError:
            # validar_env ausente: cai na checagem basica abaixo em vez de travar.
            pass
        except RuntimeError as e:
            raise ValueError(str(e))

        if not self.url or not self.username or not self.password:
            raise ValueError('Credenciais de Portainer incompletas no arquivo .env (PORTEINER_URL, USERNAME, PASSWORD).')

    def authenticate(self):
        auth_url = f"{self.url}/api/auth"
        payload = {'Username': self.username, 'Password': self.password}
        try:
            res = requests.post(auth_url, json=payload, verify=VERIFICAR_TLS, timeout=15)
            if res.status_code == 200:
                self.jwt = res.json().get('jwt')
                return True
            else:
                raise ConnectionError(f"FALHA na autenticacao do Portainer (HTTP {res.status_code}): {res.text}")
        except Exception as e:
            raise ConnectionError(f"Erro ao conectar com Portainer em {auth_url}: {str(e)}")

    def _headers(self):
        if not self.jwt:
            self.authenticate()
        return {'Authorization': f"Bearer {self.jwt}"}

    def get_endpoints(self):
        url = f"{self.url}/api/endpoints"
        res = requests.get(url, headers=self._headers(), verify=VERIFICAR_TLS, timeout=15)
        res.raise_for_status()
        return res.json()

    def get_stacks(self):
        url = f"{self.url}/api/stacks"
        res = requests.get(url, headers=self._headers(), verify=VERIFICAR_TLS, timeout=15)
        res.raise_for_status()
        return res.json()

    def get_containers(self, endpoint_id=1):
        url = f"{self.url}/api/endpoints/{endpoint_id}/docker/containers/json?all=1"
        res = requests.get(url, headers=self._headers(), verify=VERIFICAR_TLS, timeout=15)
        res.raise_for_status()
        return res.json()

    def get_services(self, endpoint_id=1):
        url = f"{self.url}/api/endpoints/{endpoint_id}/docker/services"
        res = requests.get(url, headers=self._headers(), verify=VERIFICAR_TLS, timeout=15)
        if res.status_code == 404:
            return []
        res.raise_for_status()
        return res.json()

    def get_networks(self, endpoint_id=1):
        url = f"{self.url}/api/endpoints/{endpoint_id}/docker/networks"
        res = requests.get(url, headers=self._headers(), verify=VERIFICAR_TLS, timeout=15)
        res.raise_for_status()
        return res.json()

    def get_volumes(self, endpoint_id=1):
        url = f"{self.url}/api/endpoints/{endpoint_id}/docker/volumes"
        res = requests.get(url, headers=self._headers(), verify=VERIFICAR_TLS, timeout=15)
        res.raise_for_status()
        return res.json()

if __name__ == '__main__':
    client = PortainerClient()
    client.authenticate()
    print('PortainerClient autenticado com sucesso!')
