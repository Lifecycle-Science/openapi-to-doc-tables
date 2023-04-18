---
id: get-get-program-status
title: "ActionHub | Get Program Status"
description: "Get the current status of a program. Status events logged currently include rebase activity."
---
# Get Program Status
<code class='method-name'><span class='get'>GET</span> /program/status</code>

Get the current status of a program. Status events logged currently include rebase activity.

## Request Parameters 

### Header Parameters  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Description</th></tr><tr><td><code>program-id</code> <span class='required'>required</span></td><td>string</td><td>



</td></tr></table>

## Responses  

### `200` Successful Response

ProgramStatus | `application/json`  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Properties</th></tr><tr><td><code>program_id</code> <span class='required'>required</span></td><td>string</td><td>


</td></tr><tr><td><code>status_id</code> <span class='required'>required</span></td><td>string</td><td>


</td></tr><tr><td><code>message</code> <span class='required'>required</span></td><td>string</td><td>


</td></tr><tr><td><code>ts_logged</code> <span class='required'>required</span></td><td>string</td><td>

description: Time the status was logged<br/>format: date-time<br/>
</td></tr></table>


**Response Example**  

```json
{
  "program_id": "string",
  "status_id": "string",
  "message": "string",
  "ts_logged": "string"
}
```

### `404` User history not found

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

