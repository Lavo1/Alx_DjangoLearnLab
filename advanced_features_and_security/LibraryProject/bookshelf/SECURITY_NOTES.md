# Security Measures Implemented

## Settings
- `DEBUG = False` for production
- Enabled XSS filtering, MIME-sniffing protection, clickjacking protection
- Cookies secured over HTTPS

## CSRF
- `{% csrf_token %}` used in all form templates
- `CSRF_COOKIE_SECURE` set to `True`

## SQL Injection
- All data access is done via Django ORM
- No raw SQL used

## XSS
- Input validation via Django forms
- CSP headers set using `django-csp`

## CSP
- django-csp middleware added
- Restricted script, style, and font sources
