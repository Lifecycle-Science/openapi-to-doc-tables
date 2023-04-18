import json

f = open('openapi.json')
source = json.loads(f.read())
f.close()

servers = source["servers"]
paths = source["paths"]
components = source["components"]
tags = source["tags"]


def kv_row(key, value):
    return f"""<th>{key}</th><td>{value}</td>"""


def servers_to_html(servers):
    """Return the server array as html
    """
    servers_html = "<table><tr><th colspan='2'>Servers</th></tr>"
    for i in servers:
        url = i["url"]
        description = i["description"]
        servers_html += f"<tr><td>{url}</td><td>{description}</td></tr>"
    servers_html += "</table>"
    return servers_html


def info_to_html(info):
    """Not included:
    - termsOfService
    - contact
    - version

    :param info: <Object>
    :return: <html>
    """
    info_html = "<table>"
    info_html += f'<tr>{kv_row("Title", info["title"])}</tr>'
    info_html += f'<tr>{kv_row("Version", info["version"])}</tr>'
    info_html += f'<tr>{kv_row("Description", info["description"])}</tr>'
    info_html += "</table>"
    return info_html


def method_line(method, path):
    safe_path = path.replace("{", "{'{").replace("}", "}'}")
    return f"<code class='method-name'><span class='{method}'>{method.upper()}</span> {safe_path}</code>"


def params_to_html(params):
    """Returns the output for the params
    including header, path, and query
    """
    header_row = "<tr><th>Name</th><th>Type</th><th>Description</th></tr>"
    required_label = " <span class='required'>required</span>"

    param_html = {}
    for p in params:

        # parse the name
        name = f'<code>{p["name"]}</code>'
        if p["required"]:
            name += required_label

        # parse the description and add the default on top
        description = ""
        if "default" in p["schema"] and p["schema"]["default"] != "":
            description += f'Default: {p["schema"]["default"]}<br/>'
        if "description" in p:
            description += p["description"]

        # parse the top
        type = ""
        if "type" in p["schema"]:
            type = p["schema"]["type"]

        # build the row
        row = f'<tr><td>{name}</td><td>{type}</td><td>\n\n{description}\n\n</td></tr>'

        # add the row to the type collection
        if p["in"] in param_html:
            param_html[p["in"]].append(row)
        else:
            param_html[p["in"]] = [row]

    # build the output
    output_html = ""
    if "path" in param_html:
        output_html += "\n### Path Parameters  \n"
        output_html += "<table class='openapi-table'>"
        output_html += header_row
        output_html += "".join(param_html["path"])
        output_html += "</table>\n\n"
    if "query" in param_html:
        output_html += "\n### Query Parameters  \n"
        output_html += "<table class='openapi-table'>"
        output_html += header_row
        output_html += "".join(param_html["query"])
        output_html += "</table>\n\n"
    if "header" in param_html:
        output_html += "\n### Header Parameters  \n"
        output_html += "<table class='openapi-table'>"
        output_html += header_row
        output_html += "".join(param_html["header"])
        output_html += "</table>\n"

    return "\n\n## Request Parameters \n" + output_html


def schema_to_html(schema_name):
    schema = components["schemas"][schema_name]

    header_row = "<tr><th>Name</th><th>Type</th><th>Properties</th></tr>"
    required_label = " <span class='required'>required</span>"
    nested_schema_html = ""

    code_obj = {}
    nested_code_obj = {}

    # array of required fields
    if "required" in schema:
        required = schema["required"]
    else:
        required = []

    row_html = ""
    for i in schema["properties"]:
        row_html += "<tr>"

        # build the name with required label if needed
        name = f'<code>{i}</code>'
        if i in required:
            name += required_label

        # for use...
        props = schema["properties"][i]

        # get the type
        prop_type = props["type"]

        row_html += f'<td>{name}</td>'
        row_html += f'<td>{prop_type}</td>'
        code_obj[i] = prop_type

        row_html += "<td>\n\n"
        for ii in props:
            if ii not in ["title", "type"]:
                try:
                    if "$ref" in props[ii]:
                        nested_schema_name = props[ii]["$ref"].rsplit('/', 1)[1]
                        nested_schema_html, nested_code_obj = schema_to_html(nested_schema_name)
                        code_obj[i] = [nested_code_obj]
                except TypeError:
                    pass

                print(ii, props[ii])
                row_html += f'{ii}: {props[ii]}<br/>'

        row_html += "\n</td>"
        row_html += "</tr>"

    output_html = F"{schema_name} | `application/json`  \n"
    output_html += "<table class='openapi-table'>" + header_row + row_html + "</table>\n\n"

    if nested_schema_html != "":
        output_html += nested_schema_html
    return output_html, code_obj


def request_body_to_html(request_body):
    output_html = "\n## Request Body  \n\n"

    schema_name = request_body["content"]["application/json"]["schema"]["$ref"].rsplit('/', 1)[1]
    html, code = schema_to_html(schema_name)
    output_html += html + '\n**Request Example**  \n\n```json\n' + json.dumps(code, indent=2) + '\n```\n'
    return output_html


def responses_to_html(responses):
    output_html = ""
    for response_code in responses:
        response = responses[response_code]
        output_html += f'\n### `{response_code}` {response["description"]}\n\n'
        try:
            schema_name = response["content"]["application/json"]["schema"]["$ref"].rsplit('/', 1)[1]
            html, code = schema_to_html(schema_name)
            output_html += html
            if (response_code == "200") and code:
                output_html += '\n**Response Example**  \n\n```json\n' + json.dumps(code, indent=2) + '\n```\n'
        except KeyError:
            # no schema
            pass

    output_html = "\n## Responses  \n" + output_html
    return output_html


# for path in paths:
def path_to_html(path_start):
    sidebar = []
    for path in paths:
        if path.startswith(path_start):
            for method in paths[path]:
                m = paths[path][method]

                # build the header portion
                output = f'# {m["summary"]}' + "\n"
                output += method_line(method, path) + "\n"
                if "description" in m:
                    output += "\n" + m["description"]

                m = paths[path][method]
                params = m["parameters"]

                # get the params output
                params_html = params_to_html(params)

                request_body_html = ""
                if "requestBody" in m:
                    request_body_html = request_body_to_html(m["requestBody"])

                responses_html = responses_to_html(m["responses"])

                # for i in m:
                #     print(i)
                #     print(m[i])
                # tags = m["tags"]

                filename = method + "-" + m["summary"].lower().replace(" ", "-")

                frontmatter = "---\n"
                frontmatter += f'id: {filename}\n'
                frontmatter += f'title: "ActionHub | {m["summary"]}"\n'
                if "description" in m:
                    frontmatter += f'description: "{m["description"]}"\n'
                frontmatter += "---\n"

                output_file = open("api/" + filename + ".md", "w")
                output_file.write(frontmatter)
                output_file.write(output)
                output_file.write(params_html)
                output_file.write(request_body_html)
                output_file.write(responses_html)
                output_file.close()

                nav_item = f"""{{
    type: "doc",
    id: "api/{filename}",
    label: "{m["summary"]}",
    className: "api-method {method}"
                }}"""
                sidebar.append(nav_item)

    filename = "api/sidebar.js"
    output_file = open(filename, "w")
    output_file.write("[" + ",\n".join(sidebar) + "]")
    output_file.close()


# path_to_html("/users")
# print(components["schemas"])

print(servers_to_html(servers))