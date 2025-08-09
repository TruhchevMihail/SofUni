def practice_members(self, guild_hall: BaseGuildHall, sessions_number: int):
    for _ in range(sessions_number):
        for member in guild_hall.members:
            member.practice()
    total_skill = sum(m.skill_level for m in guild_hall.members)
    return f"{guild_hall.alias} members have {total_skill} total skill level after {sessions_number} practice session/s."


def unassign_member(self, guild_hall: BaseGuildHall, member_tag: str):
    member = next((m for m in guild_hall.members if m.tag == member_tag), None)
    if not member or member.skill_level >= 10:
        return "The unassignment process was canceled."

    guild_hall.members.remove(member)
    self.members.append(member)
    return f"Unassigned member {member_tag}."


def guild_update(self, min_skill_level_value: int):
    for hall in self.guild_halls:
        hall.increase_gold(min_skill_level_value)

    sorted_halls = sorted(self.guild_halls,
                          key=lambda x: (-len(x.members), x.alias))

    result = ["<<<Guild Updated Status>>>",
              f"Unassigned members count: {len(self.members)}",
              f"Guild halls count: {len(self.guild_halls)}"]

    for hall in sorted_halls:
        result.append(hall.status())

    return "\n".join(result)