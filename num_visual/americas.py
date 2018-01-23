import pygal

vm = pygal.maps.world.World()

vm.title = 'Population of Contries in North America'
vm.add('North America',{'ca':34126000,'us':309349000,'mx':113423000})
vm.render_to_file('na_populations.svg')
'''
vm.title = 'North, Central, and South America'

vm.add('North America',['ca','mx','us'])
vm.add('Central America',['bz','cr','gt','hn','ni','pa','sv'])
vm.add('South America', ['ar','bo','br','cl','co','ec','gf'])

vm.render_to_file('americas.svg')
'''
