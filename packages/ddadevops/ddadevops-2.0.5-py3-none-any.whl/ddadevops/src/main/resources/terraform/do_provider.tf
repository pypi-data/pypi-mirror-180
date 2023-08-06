provider "digitalocean" {
  token = var.do_api_key
  spaces_access_id = var.spaces_secret_key
  spaces_secret_key = var.spaces_secret_key
}
