# skill-atoms

Catalog of AI skills — discoverable, invocable units of capability that agents and runtimes load on demand. Part of the [convergent-systems-co](https://github.com/convergent-systems-co) atoms ecosystem.

| | |
|---|---|
| **Type** | `skill` (per [atoms type taxonomy v0.1](https://github.com/convergent-systems-co/atoms/blob/main/docs/superpowers/specs/2026-05-23-atoms-type-taxonomy-design.md)) |
| **Site** | [`skill-atoms.com`](https://skill-atoms.com) (apex, Cloudflare-proxied) |
| **Catalog content** | `skills/` (empty — additions begin once the skill schema lands in schema-atoms) |
| **Ecosystem** | Federated under `xdao.co` |

## Status

Bootstrap state. The repo exists with the standard atoms scaffold; the catalog is empty. Skills will be authored once the canonical `skill` schema is published in [schema-atoms](https://github.com/convergent-systems-co/schema-atoms) (sub-project 2).

## Layout

```
skills/                         catalog content (empty — skills land here)
schemas/                        local schema references; canonical schemas live in schema-atoms
web/site/                       Astro static site → skill-atoms.convergent-systems.co
infra/terraform/                Cloudflare Pages + DNS via core-infra v0.1.0 pages-project module
.github/workflows/              CI: build, tf-plan, secret-scan, release-to-pages
ATOMS.yml                       catalog manifest (conforms to atoms-spec/v1)
```

## Deployment state

| Layer | Status |
|---|---|
| GitHub repo | live |
| Submodule registered in parent atoms | via `convergent-systems-co/atoms` branch `chore/bootstrap-skill-atoms` |
| Astro site build | template-state placeholder |
| Cloudflare Pages project | provisioned via `infra/terraform/envs/prod` |
| `skill-atoms.com` apex DNS | wired (CNAME → `skill-atoms.pages.dev`, proxied) |
| Site deploy | direct-upload via `wrangler pages deploy` from CI |

## Local development

```bash
cd web/site
npm install
npm run dev
```

## License

Apache-2.0. See [LICENSE](LICENSE).
