---
id: get-get-user-events-log
title: "ActionHub | Get User Events Log"
description: "Get the raw action history log for the given user."
---
# Get User Events Log
<code class='method-name'><span class='get'>GET</span> /users/{'{user_id}'}/events</code>

Get the raw action history log for the given user.

## Request Parameters 

### Path Parameters  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Description</th></tr><tr><td><code>user_id</code> <span class='required'>required</span></td><td>string</td><td>



</td></tr></table>


### Header Parameters  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Description</th></tr><tr><td><code>program-id</code> <span class='required'>required</span></td><td>string</td><td>



</td></tr></table>

## Responses  

### `200` Successful Response

UserRawHistoryActionList | `application/json`  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Properties</th></tr><tr><td><code>history</code> <span class='required'>required</span></td><td>array</td><td>

items: {'$ref': '#/components/schemas/UserRawHistoryAction'}<br/>
</td></tr></table>

UserRawHistoryAction | `application/json`  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Properties</th></tr><tr><td><code>timestamp</code> <span class='required'>required</span></td><td>string</td><td>

description: Time of event in ISO 8601 format<br/>format: date-time<br/>
</td></tr><tr><td><code>event_type</code> <span class='required'>required</span></td><td>string</td><td>

description: The behavior logged in the action<br/>
</td></tr><tr><td><code>asset_id</code> <span class='required'>required</span></td><td>string</td><td>


</td></tr><tr><td><code>asset_name</code> <span class='required'>required</span></td><td>string</td><td>


</td></tr><tr><td><code>event_labels</code></td><td>array</td><td>

items: {}<br/>
</td></tr><tr><td><code>asset_labels</code></td><td>array</td><td>

items: {}<br/>
</td></tr></table>


**Response Example**  

```json
{
  "history": [
    {
      "timestamp": "string",
      "event_type": "string",
      "asset_id": "string",
      "asset_name": "string",
      "event_labels": "array",
      "asset_labels": "array"
    }
  ]
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

