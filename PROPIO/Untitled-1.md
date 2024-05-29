curl -iX POST \
 'http://localhost:4041/iot/services' \
 -H 'Content-Type: application/json' \
 -H 'fiware-service: openiot' \
 -H 'fiware-servicepath: /' \
 -d '{
"services": [

{
"entities": [
{
"type": "Entidad_tipo",
"isPattern": "false",
"id": "Entidad_id",
}
],
attributes": [
"attr1"
]

    "updateAction": "APPEND"

}

]
}'
