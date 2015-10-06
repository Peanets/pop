import click
from pop.exceptions.no_project_error import NoProjectError
from sklearn.decomposition import PCA
from pop.utils.decorators import project_exists, data_exists
import matplotlib.pyplot as plt

@click.command('pca', short_help='Principal Component Analysis of data')
@click.argument('nb_dim', required=False, type=int)
@click.pass_obj
@project_exists
@data_exists
def cli(ctl,nb_dim):
	data = ctl.get_table()
	pca = PCA(n_components=nb_dim)
	pca.fit(data)

	plt.figure(1, figsize=(4, 3))
	plt.clf()
	plt.plot(pca.explained_variance_, linewidth=2)
	plt.axis('tight')
	plt.xlabel('n_components')
	plt.ylabel('explained_variance_')
	plt.show()