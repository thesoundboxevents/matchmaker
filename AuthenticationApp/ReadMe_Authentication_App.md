## Configuration

The AuthenticationApp acts as the central pillar for user authentication across the Project-Musica, offering backend support for apps like `NewUserApp` and utilizing forms from `ProfilesApp` for a seamless user experience. This app does not serve HTML files directly; instead, it provides the underlying authentication logic that other apps can utilize.

### Environment Variables
The AuthenticationApp relies on specific environment variables that should be set to ensure secure and proper operation:

- `DJANGO_SECRET_KEY`: Essential for security, used for hashing and cryptographic operations.
- `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_USE_TLS`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`: Configuration for the email server to send out system-generated emails.

### Django Settings
Configure the Django settings to tie the AuthenticationApp with the overall project:

- `AUTHENTICATION_BACKENDS`: List the backends used for authentication, including any custom backends if necessary.
- `AUTH_PASSWORD_VALIDATORS`: Define password strength validators that align with your security policies.
- `EMAIL_BACKEND`: Set the backend to facilitate email sending functionalities for user verification and password resets.

### Security Settings
Since the AuthenticationApp handles sensitive user data, these security settings are vital:

- `SESSION_COOKIE_SECURE`: Ensure this is set to `True` to use cookies only over HTTPS.
- `CSRF_COOKIE_SECURE`: Set to `True` to secure CSRF cookies over HTTPS.
- `SECURE_BROWSER_XSS_FILTER`: Enable this for additional cross-site scripting protection in browsers.

### Integration Points
This app is designed to work in conjunction with other apps:

- `NewUserApp`: The AuthenticationApp provides backend authentication processes for the `NewUserApp`.
- `ProfilesApp`: Subsequently, user profile forms and data management are handled within `ProfilesApp`, with authentication processes supported by the AuthenticationApp.

### Custom User Model
If there's a custom user model involved in the project:

```python
AUTH_USER_MODEL = 'ProfilesApp.CustomUser'
