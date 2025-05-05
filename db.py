import aiosqlite

DB_PATH = "ranking.db"

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS ranking (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                pontos INTEGER DEFAULT 1000,
                vitorias INTEGER DEFAULT 0,
                derrotas INTEGER DEFAULT 0
            );
        """)
        await db.commit()

        # Inserir dados fictícios se tabela estiver vazia
        cursor = await db.execute("SELECT COUNT(*) FROM ranking;")
        count = (await cursor.fetchone())[0]
        if count == 0:
            jogadores = [
                ("Ash", 1200, 10, 3),
                ("Misty", 1150, 8, 4),
                ("Brock", 1100, 7, 5),
                ("Gary", 1300, 12, 2),
                ("May", 1080, 6, 6),
                ("Dawn", 1020, 4, 7),
            ]
            await db.executemany("INSERT INTO ranking (nome, pontos, vitorias, derrotas) VALUES (?, ?, ?, ?);", jogadores)
            await db.commit()

async def get_ranking():
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("""
            SELECT nome, pontos, vitorias, derrotas
            FROM ranking
            ORDER BY pontos DESC
            LIMIT 10;
        """)
        rows = await cursor.fetchall()
        return rows
