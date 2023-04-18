---
id: post-post-assets
title: "ActionHub | Post Assets"
description: "For each of the assets in the list of provided assets, upsert function will either add new asset to program, or update existing asset with the same asset_id"
---
# Post Assets
<code class='method-name'><span class='post'>POST</span> /assets</code>

For each of the assets in the list of provided assets, upsert function will either add new asset to program, or update existing asset with the same asset_id

## Request Parameters 

### Header Parameters  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Description</th></tr><tr><td><code>program-id</code> <span class='required'>required</span></td><td>string</td><td>



</td></tr></table>

## Request Body  

AssetList | `application/json`  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Properties</th></tr><tr><td><code>assets</code> <span class='required'>required</span></td><td>array</td><td>

items: {'$ref': '#/components/schemas/Asset'}<br/>
</td></tr></table>

Asset | `application/json`  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Properties</th></tr><tr><td><code>asset_id</code> <span class='required'>required</span></td><td>string</td><td>

maxLength: 64<br/>
</td></tr><tr><td><code>asset_name</code></td><td>string</td><td>

maxLength: 124<br/>
</td></tr><tr><td><code>labels</code></td><td>array</td><td>

items: {}<br/>
</td></tr></table>


**Request Example**  

```json
{
  "assets": [
    {
      "asset_id": "string",
      "asset_name": "string",
      "labels": "array"
    }
  ]
}
```

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

