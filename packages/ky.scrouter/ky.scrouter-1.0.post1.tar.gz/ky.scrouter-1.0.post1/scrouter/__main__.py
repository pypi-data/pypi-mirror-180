import scrouter.agent as agent
a, b = input('We will trace route from (lowest who?) '), input('and (highest who?) ')
print('')
agent.route(a.strip().casefold(), b.strip().casefold())
