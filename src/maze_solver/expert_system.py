"""Small rule-based expert system that explains maze-search results."""

from .algorithms import SearchResult


def diagnose(result: SearchResult, algorithm: str, start: tuple[int, int], goal: tuple[int, int]) -> str:
    """Return a human-readable explanation based on explicit IF-THEN rules."""
    if start == goal:
        return "IF titik awal sama dengan tujuan, THEN tujuan sudah tercapai. Tidak perlu bergerak."

    if not result.found:
        return (
            "IF tidak ada jalur yang ditemukan, THEN titik tujuan tidak dapat dijangkau "
            "dari titik awal pada peta saat ini. Periksa apakah dinding memutus semua jalur, "
            "lalu hapus atau ubah beberapa dinding dan jalankan pencarian lagi."
        )

    if algorithm.upper() == "BFS":
        return (
            "IF BFS menemukan jalur pada labirin dengan biaya setiap langkah yang sama, "
            "THEN jalur tersebut merupakan jalur dengan jumlah langkah minimum."
        )
    if algorithm.upper() == "DFS":
        return (
            "IF DFS menemukan jalur, THEN tujuan dapat dijangkau. Namun, DFS menelusuri "
            "satu cabang lebih dalam terlebih dahulu, sehingga jalurnya belum tentu paling pendek. "
            "Gunakan BFS jika ingin membandingkan jumlah langkah minimum."
        )
    return "Jalur ditemukan. Periksa jumlah langkah dan simpul yang dikunjungi untuk memahami hasil pencarian."
