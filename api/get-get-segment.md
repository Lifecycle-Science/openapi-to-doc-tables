---
id: get-get-segment
title: "ActionHub | Get Segment"
description: "Get plaintext list of user_ids matching segment criteria. See product documentations for full description of segment criteria."
---
# Get Segment
<code class='method-name'><span class='get'>GET</span> /segment</code>

Get plaintext list of user_ids matching segment criteria. See product documentations for full description of segment criteria.

## Request Parameters 

### Query Parameters  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Description</th></tr><tr><td><code>asset_ids</code></td><td>string</td><td>

Comma delimited list of asset ids to use as the bases for the segment. Users with growth value recommendations for the supplied asset ids will be included in the segment. Either asset_ids  or labels must be provided for segments. If asset_ids are provided labels are ignored.

</td></tr><tr><td><code>labels</code></td><td>string</td><td>

Comma delimited list of labels to use as the bases for the segment. Users with growth value recommendations for the supplied labels ids will be included in the segment. Either asset_ids or labels must be provided for segments. If asset_ids are provided labels are ignored.

</td></tr><tr><td><code>action_types</code></td><td>string</td><td>

Optional comma delimited list of recommended action types (same list as event types) to use as a recommendations FILTER for the asset list provided. Only asset recommendations of the provided action types will be included in the segment.

</td></tr><tr><td><code>match_type</code></td><td></td><td>

Default: any<br/>Indicates if membership in the segment requires match for all assets/labels or any (default).

</td></tr><tr><td><code>segment_type</code></td><td></td><td>

Default: growth<br/>Indicates if the segment should consider all growth values (default), only values matching a user history (base), or only values that are net new for the user (discovery).See product documentation for more details about segment types

</td></tr><tr><td><code>min_weight</code></td><td>number</td><td>

Default: 0.5<br/>Minimum weight allowable for asset and label recommendations to qualify for the segment.

</td></tr><tr><td><code>force_refresh</code></td><td>boolean</td><td>

Default: False<br/>Recalculate the segment and do not use the cache

</td></tr></table>


### Header Parameters  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Description</th></tr><tr><td><code>program-id</code> <span class='required'>required</span></td><td>string</td><td>



</td></tr></table>

## Responses  

### `200` Successful Response


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

