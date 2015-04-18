#!/usr/bin/python
# helpful org list found here:
# https://github.com/hzlzh/Domain-Name-List/blob/master/org-words.txt
import random

nonprofit_list = [
    "National Public Radio", "United Nations Children's Fund",
    "Human Rights Watch", "WikiLeaks", "Green Peace",
    "Smithsonian Institute", "Human Rights Campaign",
    "Charity: water", "Kiva", "American Museum of Natural History",
    "Doctors Without Borders", "Rotary Foundation of Rotary International",
    "Sierra Club", "Feeding America", "New York Public Library",
    "Natural Resources Defense Council", "Metropolitan Museum of Art", "Oxfam",
    "Do Something", "Planned Parenthood Federation of America",
    "Wikimedia Foundation",
    "Environmental Defense", "Monterey Bay Aquarium", "Save the Children",
    "Teach for America", "United States Fund for UNICEF",
    "The Trevor Project", "Alzheimer's Association",
    "International Rescue Committee", "Conservation International Foundation",
    "Water.org", "Museum of Modern Art",
    "Oxfam America", "Friends of the National Zoo", "American Red Cross",
    "Disabled American Veterans", "Lions Clubs International Foundation",
    "National FFA Foundation", "Ronald McDonald House Charities",
    "National Council of YMCAs of the USA", "Samaritan's Purse",
    "Billy Graham Evangelistic Association", "National 4-H Council",
    "United States Olympic Committee", "World Wildlife Fund",
    "Zoological Society of San Diego",
    "American Society for the Prevention of Cruelty to orgs",
    "Goodwill", "Lincoln Center for Performing Arts", "Arthritis Foundation",
    "Compassion International", "Council on Foreign Relations",
    "Partners In Health", "St. Jude's Children's Research Hospital",
    "World Food Program USA", "Stand Up To Cancer",
    "Dana-Farber Cancer Institute", "Wounded Warrior Project",
    "Creative Commons", "International Committee of the Red Cross",
    "Global Giving", "Susan G Komen Breast Cancer Foundation",
    "World Vision USA", "Food & Water Watch", "Room to Read", "ACLU", "Ashoka",
    "Operation Blessing International Relief", "Habitat for Humanity",
    "Girl Scouts of the USA", "Alley Cat Allies", "PetSmart Charities",
    "Art Institute of Chicago", "National Audubon Society",
    "JFK Center for Performing Arts", "Farm Sanctuary", "Big Cat Rescue",
    "International Justice Mission", "Focus on the Family", "USO",
    "Aquarium of the Pacific", "Make-A-Wish", "Operation Homefront",
    "Cincinnati Zoo & Botanical Garden", "World Wildlife Fund",
    "The 92nd Street Y", "The Center for Strategic and International Studies",
    "Carter Center", "Human Rights First",
    "Alex's Lemonade Stand Foundation", "Museum of Fine Arts",
    "Boys & Girls Clubs of America", "National Aquarium",
    "World Vision", "TED", "American Heart Association", "United Way",
    "Defenders of Wildlife", "Public Broadcasting Service", "Kaboom"]

mission_list = [
    "inspire", "spread", "increase", "decrease", "effect", "bring", "serve",
    "conserve", "improve", "empower", "honor", "create", "find", "support",
    "preserve", "educate", "inform", "build", "work with", "end", "care for",
    "provide", "connect", "advance", "strengthen", "help", "research", "lead",
    "grow", "enhance", "protect", "fight", "engage", "steward",
    "enrich", "alleviate", "seek", "mobilize", "prepare", "advocate"]

longevity_list = [
    "permanent", "lasting", "lifelong", "temporary", "continuing",
    "immediate", "scaleable"]

vision_list = [
    "informed public", "world understanding", "goodwill",
    "change", "diffusion of knowledge",
    "health, education, and economic opportunities", "social justice",
    "solutions", "a cure", "healthier lives",
    "prevention of cruelty",
    "learning", "communities", "clean drinking water",
    "equality", "alleviation of poverty", "medical aid", "safe spaces",
    "free speech"]

constituent_list = [
    "kids", "children", "future generations", "people", "the elderly",
    "vulnerable communities", "marginalized populations", "familes",
    "communities", "animals", "birds", "oceans", "habitats", "wetlands",
    "forests", "young people", "veterans", "wounded warriors"]

type_list = [
    'a nonprofit startup', 'a collaborative working group',
    'a 501c3', 'a political advocacy group',
    'a think tank', 'a nonprofit charity', 'a private foundation',
    'a grassroots organization', 'a research center']


def org():
    return (random.choice(nonprofit_list))


def typeorg():
    return (random.choice(type_list))


def constituent():
    return (random.choice(constituent_list))


def longevity():
    return (random.choice(longevity_list))


def mission():
    return (random.choice(mission_list))


def vision():
    return (random.choice(vision_list))


def prefix():
    source_org = str((random.choice(nonprofit_list)))
    x = len(source_org)
    numwords = source_org.count(" ") + 1
    if numwords > 1:
        pre = source_org.split(" ", 2)
        pre = str(pre[0] + " " + pre[1])
    else:
        pre = source_org[:x / 2]
    if x > 9:
        return [source_org, x, pre]
    else:
        return [source_org, x, source_org]


def suffix():
    source_org = str((random.choice(nonprofit_list)))
    x = len(source_org)
    # how many words?
    numwords = source_org.count(" ") + 1
    if numwords > 1:
        suf = source_org.rsplit(" ", 2)
        suf = str(suf[-2] + " " + suf[-1])
    else:
        suf = source_org[-x / 2:]
    if x > 9:
        return [source_org, x, suf]
    else:
        return [source_org, x, source_org]


def new_org_data():
    org1 = prefix()
    org2 = suffix()
    new_org_name = org1[2] + " " + org2[2]
    extended_description = (
        new_org_name.upper(), 'is', typeorg(), 'with a mission to', mission(), 'and',
        mission(), longevity(),
        vision(), 'for', constituent() +
        '.')
    return [new_org_name, extended_description]


def create_nonprofit_list(x=10):
    count = 0
    nonprofit_list = []
    while count < x:
        new_org = new_org_data()
        description = ' '.join(new_org[1])
        the_org_info = '{d}'.format(d=description)
        nonprofit_list.append(the_org_info)
        count += 1
    return (nonprofit_list)

# Main funciton


def main(howmany):
    text = '\n'.join(sorted(create_nonprofit_list(howmany)))
    print text
    with open('workfile.txt', 'w') as f:
        f.write(text)

# EXECUTE
main(100)
