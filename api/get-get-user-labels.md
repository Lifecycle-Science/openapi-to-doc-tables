---
id: get-get-user-labels
title: "ActionHub | Get User Labels"
description: "Get a collection of labels and their weights used in recommendations for the given user. The higher weight values indicate higher user engagement. Results are order by highest-lowest weight values."
---
# Get User Labels
<code class='method-name'><span class='get'>GET</span> /users/{'{user_id}'}/labels</code>

Get a collection of labels and their weights used in recommendations for the given user. The higher weight values indicate higher user engagement. Results are order by highest-lowest weight values.

## Request Parameters 

### Path Parameters  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Description</th></tr><tr><td><code>user_id</code> <span class='required'>required</span></td><td>string</td><td>



</td></tr></table>


### Header Parameters  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Description</th></tr><tr><td><code>program-id</code> <span class='required'>required</span></td><td>string</td><td>



</td></tr></table>

## Responses  

### `200` Successful Response

UserLabelDict | `application/json`  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Properties</th></tr><tr><td><code>labels</code> <span class='required'>required</span></td><td>object</td><td>

description: An array of key-value pairs containing `label`:`weight`<br/>
</td></tr></table>


**Response Example**  

```json
{
  "labels": "object"
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

