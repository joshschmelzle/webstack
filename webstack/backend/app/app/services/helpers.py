import asyncio


async def run_cli_async(cmd: str) -> str:
    proc = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )

    stdout, stderr = await proc.communicate()

    if proc.returncode == 0:
        if stdout:
            return stdout.decode()

    if stderr:
        raise f"[stderr]\n{stderr.decode()}"
