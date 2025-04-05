## Long-Term Security Improvements for GitHub Actions  

### Govern Third-Party Services

- Implement vetting procedures for external actions, requiring approval before integration.  
- Restrict actions to verified sources (e.g., GitHub Marketplace "Verified Creator" badges).  

### Strict Pipeline-Based Access Controls (PBAC)

- Grant minimal permissions to workflows (e.g., least-privilege `GITHUB_TOKEN`).  
- Replace long-lived secrets with short-lived, fine-grained tokens or OpenID Connect (OIDC).  
- Isolate self-hosted runners and restrict external PR execution.  

### Pin GitHub Actions

- Avoid tags/branches (e.g., `@v3`); use full-length commit SHA-1 hashes to prevent tampering.  
- Audit action source code for secret handling and unintended data exposure.  

### Additional Measures

- Monitor workflow logs for Base64-encoded secrets.  
- Use Dependabot to update vulnerable actions.  
- Avoid `pull_request_target` for external PRs to prevent build-step abuse.  

For deeper insights, consult the [OWASP Top 10 CI/CD Security Risks](https://owasp.org/www-project-top-10-ci-cd-security-risks/).
