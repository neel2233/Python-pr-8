import Show
import Info
import DelNaN
import MakeDS

file = input('Введите полный путь к csv файлу: ')

Show.Show(file, 'random')
Info.Info(file)
DelNaN.DelNaN(file)
MakeDS.MakeDS(file)
