def sort_games(*args, **kwargs):
    title_to_id = {}
    for release_id, title in kwargs.items():
        title_to_id[title] = release_id
        
    console_games = []
    pc_games = []
    
    for game in args:
        platform, title = game
        if title in title_to_id:
            release_id = title_to_id[title]
            if platform == "console":
                console_games.append((release_id, title))
            elif platform == "pc":
                pc_games.append((release_id, title))
                
    console_games.sort(key=lambda x: x[0])
    pc_games.sort(key=lambda x: x[0], reverse=True)
    
    lines = []
    if console_games:
        lines.append("Console Games:")
        for release_id, title in console_games:
            release_date = release_id.rsplit('_', 1)[0]
            lines.append(f">>>{release_date}: {title}")
            
    if pc_games:
        lines.append("PC Games:")
        for release_id, title in pc_games:
            release_date = release_id.rsplit('_', 1)[0]
            lines.append(f"<<<{release_date}: {title}")
            
    return "\n".join(lines)

print(sort_games(
    ("pc", "Iron Comet"),
    ("console", "Jungle Quest"),
    ("console", "Cyber Realm"),
    ("pc", "Neon Skyline"),
    ("console", "Blade Echo"),
    ("pc", "Sky Frontier"),
    April_12_2025_002="Neon Skyline",
    July_01_2025_004="Cyber Realm",
    July_01_2025_002="Blade Echo",
    December_31_2024_007="Jungle Quest",
    April_12_2025_005="Iron Comet",
    February_14_2025_009="Sky Frontier",
))