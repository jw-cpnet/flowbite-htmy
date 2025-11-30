# Using GitLab Private Package Registry

This guide shows how to publish and install flowbite-htmy from your private GitLab Package Registry.

## 📦 Registry Information

- **Project ID**: `76216903`
- **Registry URL**: https://gitlab.com/et2010/flowbite-htmy/-/packages
- **PyPI Repository**: `https://gitlab.com/api/v4/projects/76216903/packages/pypi`

## Publishing to Registry

### Step 1: Build the Package

```bash
python -m build
```

This creates:
- `dist/flowbite_htmy-0.3.0.tar.gz` (source)
- `dist/flowbite_htmy-0.3.0-py3-none-any.whl` (wheel)

### Step 2: Create Access Token

**Option A: Personal Access Token (Recommended)**

1. Go to https://gitlab.com/-/user_settings/personal_access_tokens
2. Create new token:
   - **Name**: "Package Publishing - flowbite-htmy"
   - **Scopes**: ✅ `api`, ✅ `write_repository`
   - **Expiration**: Set as needed (or never)
3. Copy the token (you'll only see it once!)

**Option B: Deploy Token**

1. Go to https://gitlab.com/et2010/flowbite-htmy/-/settings/repository
2. Expand "Deploy tokens"
3. Create new token:
   - **Name**: "Package Publishing"
   - **Scopes**: ✅ `write_package_registry`
4. Copy username and token

### Step 3: Configure PyPI Credentials

Create or update `~/.pypirc`:

```ini
[distutils]
index-servers =
    gitlab

[gitlab]
repository = https://gitlab.com/api/v4/projects/76216903/packages/pypi
username = __token__
password = YOUR_PERSONAL_ACCESS_TOKEN_HERE
```

### Step 4: Publish

```bash
python -m twine upload --repository gitlab dist/*
```

Or publish directly without `.pypirc`:

```bash
python -m twine upload \
  --repository-url https://gitlab.com/api/v4/projects/76216903/packages/pypi \
  --username __token__ \
  --password YOUR_TOKEN_HERE \
  dist/*
```

## Installing from Private Registry

### For Individual Developers

#### Option 1: Using pip with credentials URL

```bash
pip install flowbite-htmy --index-url https://__token__:YOUR_TOKEN@gitlab.com/api/v4/projects/76216903/packages/pypi/simple
```

#### Option 2: Configure pip permanently

Create or update `~/.config/pip/pip.conf`:

```ini
[global]
extra-index-url = https://__token__:YOUR_TOKEN@gitlab.com/api/v4/projects/76216903/packages/pypi/simple
```

Then install normally:

```bash
pip install flowbite-htmy
```

#### Option 3: Using environment variables

```bash
export PIP_EXTRA_INDEX_URL=https://__token__:YOUR_TOKEN@gitlab.com/api/v4/projects/76216903/packages/pypi/simple
pip install flowbite-htmy
```

### For CI/CD Pipelines

Add to your `.gitlab-ci.yml`:

```yaml
variables:
  PIP_INDEX_URL: https://gitlab-ci-token:${CI_JOB_TOKEN}@gitlab.com/api/v4/projects/76216903/packages/pypi/simple

install:
  script:
    - pip install flowbite-htmy
```

### For Docker Builds

In your `Dockerfile`:

```dockerfile
ARG GITLAB_TOKEN
RUN pip install flowbite-htmy \
  --index-url https://__token__:${GITLAB_TOKEN}@gitlab.com/api/v4/projects/76216903/packages/pypi/simple
```

Build with:

```bash
docker build --build-arg GITLAB_TOKEN=YOUR_TOKEN .
```

### For requirements.txt

Create `requirements.txt`:

```txt
--extra-index-url https://__token__:YOUR_TOKEN@gitlab.com/api/v4/projects/76216903/packages/pypi/simple
flowbite-htmy==0.3.0
```

Then:

```bash
pip install -r requirements.txt
```

**⚠️ Security Note**: Never commit tokens to git! Use environment variables or CI/CD secrets.

### For Poetry

Add to `pyproject.toml`:

```toml
[[tool.poetry.source]]
name = "gitlab"
url = "https://gitlab.com/api/v4/projects/76216903/packages/pypi/simple"
priority = "supplemental"
```

Configure credentials:

```bash
poetry config http-basic.gitlab __token__ YOUR_TOKEN
```

Install:

```bash
poetry add flowbite-htmy
```

## Verifying Published Packages

View packages at:
https://gitlab.com/et2010/flowbite-htmy/-/packages

Or using API:

```bash
curl --header "PRIVATE-TOKEN: YOUR_TOKEN" \
  "https://gitlab.com/api/v4/projects/76216903/packages"
```

## Updating Packages

To publish a new version:

1. Update version in `pyproject.toml`
2. Build: `python -m build`
3. Upload: `python -m twine upload --repository gitlab dist/*`

GitLab will automatically create new package versions.

## Deleting Packages

Go to https://gitlab.com/et2010/flowbite-htmy/-/packages and delete specific versions.

Or via API:

```bash
curl --request DELETE --header "PRIVATE-TOKEN: YOUR_TOKEN" \
  "https://gitlab.com/api/v4/projects/76216903/packages/:package_id"
```

## Token Security Best Practices

1. **Use Deploy Tokens for CI/CD** - More limited scope than personal tokens
2. **Set Expiration Dates** - Rotate tokens regularly
3. **Use CI/CD Variables** - Store tokens in GitLab CI/CD settings, not in code
4. **Separate Tokens** - Different tokens for different purposes (publishing vs. installing)
5. **Read-Only When Possible** - Installing only needs `read_api` scope

## Troubleshooting

### 403 Forbidden when uploading

- Check token has `api` and `write_repository` scopes
- Verify project ID is correct (76216903)
- Ensure you're using `__token__` as username

### Package not found when installing

- Verify package was uploaded successfully
- Check token has at least `read_api` scope
- Ensure URL includes `/simple` at the end
- Try using `--index-url` instead of `--extra-index-url`

### SSL Certificate errors

Add `--trusted-host gitlab.com` to pip command:

```bash
pip install flowbite-htmy \
  --index-url https://__token__:TOKEN@gitlab.com/api/v4/projects/76216903/packages/pypi/simple \
  --trusted-host gitlab.com
```

## Benefits of Private Registry

✅ **Full Control** - Host your library privately without public PyPI
✅ **Free** - Included in GitLab Free tier (10 GB storage)
✅ **Integrated** - Same auth as your GitLab account
✅ **CI/CD Ready** - Use `CI_JOB_TOKEN` in pipelines
✅ **Version Control** - Track all published versions
✅ **Team Access** - Control who can install/publish via GitLab permissions

## Next Steps

- Set up automated publishing in GitLab CI/CD
- Create read-only tokens for team members
- Configure your local development environment
- Update project documentation with installation instructions
