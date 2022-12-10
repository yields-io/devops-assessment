# DevOps assignment

In order to apply, please duplicate the repository as described here: https://docs.github.com/en/repositories/creating-and-managing-repositories/duplicating-a-repository and send us a note at hr@yields.io

Minimal environment with `keycloak` and a custom `python` app behind
`nginx`, in `docker`, orchestrated with `docker-compose`.

## Development

Start the environment: `docker-compose up -d`

Create a new user in the `keycloak` admin: http://localhost/keycloak/admin

**_Tip_**: add credentials for `keycloak` and `postgres` in a `.env` file.

### Endpoints

1. http://localhost/: "Hello world!" index page
1. http://localhost/login: redirects to `keycloak` auth
1. http://localhost/auth/callback: `keycloak` callback after login

### Known issues

1. The `python` app builds correctly but does not work in production mode
only in development mode.
1. The app's `login` is broken.
1. Connections to the `keycloak` endpoints fail with "502 Bad Gateway".
1. The `python` app's `Dockerfile` does not follow best practices.

### Notes

1. Any `git` commits should follow the
[conventional commits](https://www.conventionalcommits.org/en/v1.0.0/)
specifications.
1. `git` formatted patches are preferred.
