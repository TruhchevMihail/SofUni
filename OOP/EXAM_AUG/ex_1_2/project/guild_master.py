from project.guild_halls.base_guild_hall import BaseGuildHall
from project.guild_members.warrior import Warrior
from project.guild_members.mage import Mage
from project.guild_halls.combat_hall import CombatHall
from project.guild_halls.magic_tower import MagicTower


class GuildMaster:
    VALID_MEMBER_TYPES = ("Warrior", "Mage")
    VALID_HALL_TYPES = ("CombatHall", "MagicTower")

    def __init__(self):
        self.members = []
        self.guild_halls = []

    def find_member_by_tag(self, tag: str, members_collection=None):
        members = self.members if members_collection is None else members_collection
        return next((m for m in members if m.tag == tag), None)

    def find_hall_by_alias(self, alias: str):
        return next((h for h in self.guild_halls if h.alias == alias), None)

    def add_member(self, member_type: str, member_tag: str, member_gold: int):
        if member_type not in self.VALID_MEMBER_TYPES:
            raise ValueError("Invalid member type!")
        if self.find_member_by_tag(member_tag) is not None:
            raise ValueError(f"{member_tag} has already been added!")

        member = Warrior(member_tag, member_gold) if member_type == "Warrior" else Mage(member_tag, member_gold)
        self.members.append(member)
        return f"{member_tag} is successfully added as {member_type}."

    def add_guild_hall(self, guild_hall_type: str, guild_hall_alias: str):
        if guild_hall_type not in self.VALID_HALL_TYPES:
            raise ValueError("Invalid guild hall type!")
        if self.find_hall_by_alias(guild_hall_alias) is not None:
            raise ValueError(f"{guild_hall_alias} has already been added!")

        hall = CombatHall(guild_hall_alias) if guild_hall_type == "CombatHall" else MagicTower(guild_hall_alias)
        self.guild_halls.append(hall)
        return f"{guild_hall_alias} is successfully added as a {guild_hall_type}."

    def assign_member(self, guild_hall_alias: str, member_type: str):
        guild_hall = self.find_hall_by_alias(guild_hall_alias)
        if not guild_hall:
            raise ValueError(f"Guild hall {guild_hall_alias} does not exist!")

        member = next((m for m in self.members if m.__class__.__name__ == member_type), None)
        if not member:
            raise ValueError("No available members of the type!")

        if len(guild_hall.members) >= guild_hall.max_member_count:
            return "Maximum member count reached. Assignment is impossible."

        self.members.remove(member)
        guild_hall.members.append(member)
        return f"{member.tag} was assigned to {guild_hall_alias}."

    def practice_members(self, guild_hall: BaseGuildHall, sessions_number: int):
        total_skill = 0
        for _ in range(sessions_number):
            for member in guild_hall.members:
                member.practice()
        for member in guild_hall.members:
            total_skill += member.skill_level
        return f"{guild_hall.alias} members have {total_skill} total skill level after {sessions_number} practice session/s."

    def unassign_member(self, guild_hall: BaseGuildHall, member_tag: str):
        member = self.find_member_by_tag(member_tag, guild_hall.members)
        if not member or member.skill_level >= 10:
            return "The unassignment process was canceled."
        guild_hall.members.remove(member)
        self.members.append(member)
        return f"Unassigned member {member_tag}."

    def guild_update(self, min_skill_level_value: int):
        for hall in self.guild_halls:
            hall.increase_gold(min_skill_level_value)

        sorted_halls = sorted(self.guild_halls, key=lambda h: (-len(h.members), h.alias))

        result = ["<<<Guild Updated Status>>>"]
        result.append(f"Unassigned members count: {len(self.members)}")
        result.append(f"Guild halls count: {len(self.guild_halls)}")

        for hall in sorted_halls:
            result.append(f">>>{hall.status()}")

        return "\n".join(result)
