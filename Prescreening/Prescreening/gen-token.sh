CLIENT_ID="appID%3ANMDPTRIAL_sandeepk_singh_nuance_com_20191213T034347371955"		   
SECRET="5HxmVA7ENxY_TaFWvo4AfEPLY8539EDCOc1YRS2tOKk"
curl -s -u "$CLIENT_ID:$SECRET" "https://auth.crt.nuance.com/oauth2/token" \
-d 'grant_type=client_credentials' -d 'scope=dlg' \
| python -c 'import sys, json; print(json.load(sys.stdin)["access_token"])' \
> my-token.txt