# Per-env variables for prod.
#
# Supply secrets via env vars, not committed values (per ~/.ai/Common.md §4):
#   export TF_VAR_cloudflare_account_id=<account-id>
#   export TF_VAR_zone_id=<zone-id-for-convergent-systems.co>
#
# Look up the zone ID in the Cloudflare dashboard:
#   dash.cloudflare.com → convergent-systems.co → Overview → "Zone ID"
#
# Then from this directory:
#   terraform init
#   terraform plan -var-file=terraform.tfvars
#   terraform apply -var-file=terraform.tfvars
