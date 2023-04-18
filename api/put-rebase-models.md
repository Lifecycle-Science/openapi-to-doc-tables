---
id: put-rebase-models
title: "ActionHub | Rebase Models"
description: "Re-calculate the base/global models used in action recommendations. In most cases, this should be done no more than once per 24 hours when (a) new products/actions/services are added to the global event store, or (b) program configuration changes have been posted and are ready for publishing. Individual user data is not impacted by this process."
---
# Rebase Models
<code class='method-name'><span class='put'>PUT</span> /program/rebase</code>

Re-calculate the base/global models used in action recommendations. In most cases, this should be done no more than once per 24 hours when (a) new products/actions/services are added to the global event store, or (b) program configuration changes have been posted and are ready for publishing. Individual user data is not impacted by this process.

## Request Parameters 

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

