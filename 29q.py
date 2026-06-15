facts = {"has_feathers", "lays_eggs"}
rules = [
    ({"has_feathers", "lays_eggs"}, "is_bird"),
    ({"is_bird", "cannot_fly", "swims"}, "is_penguin")
]

def forward_chain(facts, rules):
    agenda = list(facts)
    while agenda:
        current = agenda.pop(0)
        for premises, conclusion in rules:
            if conclusion not in facts and premises.issubset(facts):
                facts.add(conclusion)
                agenda.append(conclusion)
    return facts

facts.add("swims")
facts.add("cannot_fly")
print(forward_chain(facts, rules))
