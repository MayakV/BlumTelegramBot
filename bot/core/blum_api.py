# This code is using the requests library for making HTTP requests.
import asyncio
import aiohttp
import json


async def get_user_info(http_client: aiohttp.ClientSession, token: str, query_id: str):
    url = "https://gateway.blum.codes/v1/user/me"
    http_client.headers["Authorization"] = f"Bearer {token}"

    try:
        response = await http_client.get(url=url)
        # response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except aiohttp.RequestException as e:
        raise f"Failed getting request: {e}"

    try:
        body = response.content
    except Exception as e:
        raise f"Failed to read response body: {e}"

    try:
        result = json.loads(body)
        return result, None
    except json.JSONDecodeError as e:
        return None, f"failed to unmarshal JSON: {e}"

    try:
        token_response = json.loads(body)
    except json.JSONDecodeError as e:
        return None, f"failed to unmarshal JSON: {e}"

    if token_response.get("message") == "Token is invalid":
        return None, "token is invalid"
    else:
        print("Failed to get user information.")
        return None, f"unexpected status code: {response.status_code}"