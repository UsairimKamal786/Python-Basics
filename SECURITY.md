Supported Versions

The following table lists the versions of the project that are actively supported with security updates:

Version	Supported
5.1.x	:white_check_mark:
5.0.x	:x:
4.0.x	:white_check_mark:
< 4.0	:x:
Security Rules

To maintain the integrity and safety of the project, all contributors and maintainers must follow these rules:

Secure Coding Practices

Avoid using deprecated functions or insecure libraries.

Always sanitize and validate input from users and external systems.

Never store passwords or API keys in plaintext — use environment variables or a secrets manager.

Dependency Management

Keep all dependencies updated to their latest stable versions.

Run vulnerability scans (e.g., with npm audit, pip-audit, or equivalent) before merging code.

Remove unused dependencies promptly.

Access Control

Use the principle of least privilege for accounts, tokens, and API keys.

Require multi-factor authentication for repository access.

Data Protection

Encrypt sensitive data both in transit (HTTPS/TLS) and at rest.

Avoid logging sensitive information (e.g., passwords, tokens, personal data).

Security Testing

Conduct security testing before each release.

Fix identified vulnerabilities before deploying to production.

Use static code analysis tools and penetration testing periodically.

Incident Response

In the event of a suspected security breach, immediately restrict access to affected systems and notify the security team.

Document the incident, investigation steps, and resolution.

Reporting a Vulnerability

If you discover a security vulnerability, please follow these steps:

Contact the Security Team
Email: security@example.com (PGP key available on request).
Do not publicly disclose the vulnerability until it has been addressed.

Provide Detailed Information
Include:

Version affected

Steps to reproduce

Potential impact

Any suggested fixes

Response Timeline

Initial acknowledgment within 48 hours.

Status updates every 5 business days until resolution.

Public disclosure coordinated with the reporter after the fix is released.
