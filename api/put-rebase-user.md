---
id: put-rebase-user
title: "ActionHub | Rebase User"
description: "Recalculate/regenerate the user graphs, action weights, and label weights for the specified user. This is operation is synchronous and should only be used when troubleshooting individual users. (User graphs are automatically regenerated when (a) new events are logged, and (b) when the base graphs are recalculated."
---
# Rebase User
<code class='method-name'><span class='put'>PUT</span> /users/{'{user_id}'}/rebase</code>

Recalculate/regenerate the user graphs, action weights, and label weights for the specified user. This is operation is synchronous and should only be used when troubleshooting individual users. (User graphs are automatically regenerated when (a) new events are logged, and (b) when the base graphs are recalculated.

## Request Parameters 

### Path Parameters  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Description</th></tr><tr><td><code>user_id</code> <span class='required'>required</span></td><td>string</td><td>



</td></tr></table>


### Header Parameters  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Description</th></tr><tr><td><code>program-id</code> <span class='required'>required</span></td><td>string</td><td>



</td></tr></table>

## Responses  

### `200` Successful Response

SuccessMessage | `application/json`  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Properties</th></tr><tr><td><code>result</code> <span class='required'>required</span></td><td>string</td><td>


</td></tr></table>


**Response Example**  

```json
{
  "result": "string"
}
```

### `404` User not found

ErrorMessage | `application/json`  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Properties</th></tr><tr><td><code>detail</code> <span class='required'>required</span></td><td>string</td><td>


</td></tr></table>


### `422` Validation Error

HTTPValidationError | `application/json`  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Properties</th></tr><tr><td><code>detail</code></td><td>array</td><td>

items: {'$ref': '#/components/schemas/ValidationError'}<br/>
</td></tr></table>

ValidationError | `application/json`  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Properties</th></tr><tr><td><code>loc</code> <span class='required'>required</span></td><td>array</td><td>

items: {'anyOf': [{'type': 'string'}, {'type': 'integer'}]}<br/>
</td></tr><tr><td><code>msg</code> <span class='required'>required</span></td><td>string</td><td>


</td></tr><tr><td><code>type</code> <span class='required'>required</span></td><td>string</td><td>


</td></tr></table>

