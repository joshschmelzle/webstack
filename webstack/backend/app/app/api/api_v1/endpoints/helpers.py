import asyncio


async def run(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )

    stdout, stderr = await proc.communicate()

    # TODO: log instead of print?
    # print(f"[{cmd!r} exited with {proc.returncode}]")

    if proc.returncode == 0:
        if stdout:
            return stdout.decode()

    if stderr:
        return f"[stderr]\n{stderr.decode()}"
