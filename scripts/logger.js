/**
 * logger.js
 * Logger minimalista com níveis: debug, info, warn, error
 */

export class Logger {
  constructor(namespace = 'app') {
    this.namespace = namespace;
  }

  debug(message, data = {}) {
    if (process.env.DEBUG) {
      console.log(
        `[${this.namespace}:debug]`,
        message,
        Object.keys(data).length > 0 ? data : ''
      );
    }
  }

  info(message, data = {}) {
    console.log(
      `[${this.namespace}:info]`,
      message,
      Object.keys(data).length > 0 ? data : ''
    );
  }

  warn(message, data = {}) {
    console.warn(
      `[${this.namespace}:warn]`,
      message,
      Object.keys(data).length > 0 ? data : ''
    );
  }

  error(message, data = {}) {
    console.error(
      `[${this.namespace}:error]`,
      message,
      Object.keys(data).length > 0 ? data : ''
    );
  }
}

export default Logger;
