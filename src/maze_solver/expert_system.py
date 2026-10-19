
"""Small rule-based expert system that explains maze-search results."""

from .algorithms import SearchResult


def diagnose(
    result: SearchResult,
    algorithm: str,
    start: tuple[int, int],
    goal: tuple[int, int],
) -> str:
    """Explain the search result using explicit IF-THEN rules."""

    if start == goal:
        return (
            "IF titik awal sama dengan tujuan, "
            "THEN tujuan sudah tercapai. Tidak perlu bergerak."
        )

    if not result.found:
        return (
            "IF tidak ada jalur yang ditemukan, "
            "THEN titik tujuan tidak dapat dijangkau dari titik awal. "
            "Periksa dinding yang mungkin memutus jalur, "
            "lalu jalankan pencarian kembali."
        )

    if algorithm.upper() == "BFS":
        return (
            "IF BFS menemukan jalur dengan biaya langkah yang sama, "
            "THEN jalur tersebut memiliki jumlah langkah minimum. "
            f"Jalur membutuhkan {result.steps} langkah dan "
            f"memeriksa {result.visited_count} simpul."
        )

    if algorithm.upper() == "DFS":
        return (
            "IF DFS menemukan jalur, THEN tujuan dapat dijangkau. "
            "Namun, jalur DFS belum tentu paling pendek. "
            "Gunakan BFS untuk mencari jalur dengan jumlah langkah minimum. "
            f"Jalur membutuhkan {result.steps} langkah dan "
            f"memeriksa {result.visited_count} simpul."
        )

    return (
        "Jalur ditemukan. "
        f"Jumlah langkah: {result.steps}. "
        f"Simpul yang diperiksa: {result.visited_count}."
    )
