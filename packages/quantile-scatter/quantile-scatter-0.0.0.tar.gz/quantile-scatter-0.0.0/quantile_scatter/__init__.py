
# 分位点散布図 [quantile_scatter]
# 【動作確認 / 使用例】

import sys
import numpy as np
from sout import sout
from matplotlib import pyplot as plt

# グループに分割
def grouping(arg_ls, group_n):
	ret_ls = [[] for _ in range(group_n)]
	for i, e in enumerate(arg_ls):
		th = i / len(arg_ls)	# 無次元化インデックス
		group_idx = int(th * group_n)
		# 格納
		ret_ls[group_idx].append(e)
	return ret_ls

# 分位点散布図の描画 [quantile_scatter]
def plot(
	x,	# 横軸数値リスト
	y,	# 縦軸数値リスト
	group_n = 20,	# 分割グループ数
	ile_ls = [0.25, 0.5, 0.75]	# どこの分位点を出すか
):
	# x昇順に整序
	zip_ls = list(zip(x, y))
	zip_ls.sort(key = lambda e: e[0])
	# グループに分割
	grouped_zip_ls = grouping(zip_ls, group_n)
	# xの取り出し
	show_x_ls = [np.mean([x for x, y in group])
		for group in grouped_zip_ls]
	# 各分位点を表示
	for ile in ile_ls:
		# その分位点の計算
		ile_value_ls = [
			np.quantile(
				[y for x, y in group],
				ile
			)
			for group in grouped_zip_ls
		]
		# 描画
		plt.plot(
			show_x_ls, ile_value_ls,
			label = str(ile),
			marker = ".", markersize = 8
		)
	plt.legend()
	plt.show()
