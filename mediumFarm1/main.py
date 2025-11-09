import moveModule
import plantModule

clear()

lista = [
['g','t','g','t','g','t','g','t','g','t','g','s','s','s','s','s','s','s','s','s','s','s'],
['t','g','t','g','t','g','t','g','t','g','t','g','t','g','t','g','t','g','t','g','t','g'],
['g','t','g','t','g','t','g','t','g','t','g','t','g','t','g','t','g','t','g','t','g','t'],
['c','g','c','g','c','g','c','g','c','g','c','g','c','g','c','g','c','g','c','g','c','g'],
['c','g','c','g','c','g','c','g','c','g','c','g','c','g','c','g','c','g','c','g','c','g'],
['c','g','c','g','c','g','c','g','c','g','c','g','c','g','c','g','c','g','c','g','c','g'],
['c','g','c','g','c','g','c','g','c','g','c','g','c','g','c','g','c','g','c','g','c','g'],
['k','k','k','k','k','g','t','g','t','g','t','g','t','g','t','g','t','g','t','g','t','g'],
['k','k','k','k','k','t','g','t','g','t','g','t','g','t','g','t','g','t','g','t','g','t'],
['k','k','k','k','k','g','t','g','t','g','t','g','t','g','t','g','t','g','t','g','t','g'],
['k','k','k','k','k','t','g','t','g','t','g','t','g','t','g','t','g','t','g','t','g','t'],
['k','k','k','k','k','g','t','g','t','g','t','s','s','s','s','s','s','s','s','s','s','s'],
['p','p','p','p','p','p','p','p','p','p','c','c','c','c','c','c','c','c','c','c','c','c'],
['p','p','p','p','p','p','p','p','p','p','c','c','c','c','c','c','c','c','c','c','c','c'],
['p','p','p','p','p','p','p','p','p','p','c','c','c','c','c','c','c','c','c','c','c','c'],
['p','p','p','p','p','p','p','p','p','p','c','c','c','c','c','c','c','c','c','c','c','c'],
['p','p','p','p','p','p','p','p','p','p','c','c','c','c','c','c','c','c','c','c','c','c'],
['p','p','p','p','p','p','p','p','p','p','c','c','c','c','c','c','c','c','c','c','c','c'],
['p','p','p','p','p','p','p','p','p','p','c','c','c','c','c','c','c','c','c','c','c','c'],
['p','p','p','p','p','p','p','p','p','p','c','c','c','c','c','c','c','c','c','c','c','c'],
['p','p','p','p','p','p','p','p','p','p','g','g','g','g','g','g','g','g','g','g','g','g'],
['p','p','p','p','p','p','p','p','p','p','g','g','g','g','g','g','g','g','g','g','g','g']
]

def main():
	if len(lista) != get_world_size() or len(lista[0]) != get_world_size():
		print("Erro Código! Tamanho atual:", get_world_size())

	while True:
		i = get_pos_y()
		j = get_pos_x()
		plantModule.safePlant(lista[i][j], 'All', 'All')
		if lista[i][j] == 'T':
			moveModule.go_to((j+1)%get_world_size(), i%get_world_size())
		else:
			moveModule.mv(get_world_size()-1, get_world_size()-1)
		
		
if __name__=="__main__":
	main()