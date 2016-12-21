set terminal jpeg
set output "pic.jpg"
#set autoscale
set logscale
set xrange[10:100000]
set yrange[.00000001:13]
set xtics(100,1000,10000,100000)
set xlabel "Heap size (items)"
set ylabel "Time (seconds)"
set title ""
plot "datapoints.txt" using 1:2 with lines title "Fibonacci Heap"
