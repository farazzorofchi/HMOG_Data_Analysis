import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('All_Activity_Gestures_Times_processed.csv')
data['time_hr'] = data['time']/1000/60/60

line = [(i+1)/100 for i in range(100)]

people_activity = pd.DataFrame(data.groupby(['people','activity'])['time_hr'].sum())
people_activity = people_activity.reset_index()

map_mean_sit = data['time_hr'][(data['activity'] == 'nav') & (data['gesture'] == 1)].mean()
read_mean_sit = data['time_hr'][(data['activity'] == 'read') & (data['gesture'] == 1)].mean()
write_mean_sit = data['time_hr'][(data['activity'] == 'write') & (data['gesture'] == 1)].mean()

map_mean_walk = data['time_hr'][(data['activity'] == 'nav') & (data['gesture'] == 2)].mean()
read_mean_walk = data['time_hr'][(data['activity'] == 'read') & (data['gesture'] == 2)].mean()
write_mean_walk = data['time_hr'][(data['activity'] == 'write') & (data['gesture'] == 2)].mean()

bins = [0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5]
plt.figure()
plt.subplot(311)
plt.hist(people_activity['time_hr'][people_activity['activity'] == 'read'], color='black', label='Reading Time Disribution', bins=bins)
plt.ylabel('Number of Users', fontsize=10)
plt.xlabel('Time (hr)', fontsize=10)
plt.legend(loc="upper right", fontsize=10)
plt.axis([0, 3.5, 0, 50])

plt.subplot(312)
plt.hist(people_activity['time_hr'][people_activity['activity'] == 'write'], color='blue', label='Writing Time Disribution', bins=bins)
plt.ylabel('Number of Users', fontsize=10)
plt.xlabel('Time (hr)', fontsize=10)
plt.legend(loc="upper right", fontsize=10)
plt.axis([0, 3.5, 0, 50])

plt.subplot(313)
plt.hist(people_activity['time_hr'][people_activity['activity'] == 'nav'], color='red', label='Navigation Time Disribution', bins=bins)
plt.ylabel('Number of Users', fontsize=10)
plt.xlabel('Time (hr)', fontsize=10)
plt.legend(loc="upper right", fontsize=10)
plt.axis([0, 3.5, 0, 50])
plt.subplots_adjust(left=0.125, bottom=0.1 , right=0.9, top=0.9, wspace=0.2, hspace=0.9 )
plt.savefig('all_activities_plot_hist.pdf', bbox_inches='tight')



plt.figure()
plt.subplot(211)
plt.plot(sorted(data['time_hr'][(data['activity'] == 'read') & (data['gesture'] == 1)]), line, color='black',label='writing time')
plt.plot(sorted(data['time_hr'][(data['activity'] == 'write') & (data['gesture'] == 1)]), line, color='blue',label='reading time')
plt.plot(sorted(data['time_hr'][(data['activity'] == 'nav') & (data['gesture'] == 1)]), line, color='red', label='navigation time')
plt.title('CDF Plot of Time while Sitting')
plt.legend(loc="lower right", fontsize = 10)

plt.annotate('mean reading time', xy=(read_mean_sit, 0.565), xytext=(0.425, 0.43),
             arrowprops=dict(facecolor='black', shrink=0.05),fontsize = 9, color='black'
             )
plt.annotate('mean writing time', xy=(write_mean_sit, 0.57), xytext=(0.9, 0.575),
             arrowprops=dict(facecolor='blue', shrink=0.05),fontsize = 10, color='blue'
             )
plt.annotate('mean mapping time', xy=(map_mean_sit, 0.598), xytext=(0.03, 0.72),
             arrowprops=dict(facecolor='red', shrink=0.05),fontsize = 9, color='red',
             )
plt.xlabel('Time (hr)', fontsize=10)
plt.axis([0, 1.75, 0, 1.05])

plt.subplot(212)
plt.plot(sorted(data['time_hr'][(data['activity'] == 'read') & (data['gesture'] == 2)]), line, color='black',label='writing time')
plt.plot(sorted(data['time_hr'][(data['activity'] == 'write') & (data['gesture'] == 2)]), line, color='blue',label='reading time')
plt.plot(sorted(data['time_hr'][(data['activity'] == 'nav') & (data['gesture'] == 2)]), line, color='red', label='navigation time')
plt.title('CDF Plot of Time while Walking')
plt.legend(loc="lower right")
plt.annotate('mean reading time', xy=(read_mean_walk, 0.545), xytext=(0.03, 0.555),
             arrowprops=dict(facecolor='black', shrink=0.05),fontsize = 9, color='black'
             )
plt.annotate('mean writing time', xy=(write_mean_walk, 0.605), xytext=(0.88, 0.615),
             arrowprops=dict(facecolor='blue', shrink=0.05),fontsize = 9, color='blue'
             )
plt.annotate('mean navigation time', xy=(map_mean_walk, 0.545), xytext=(0.6, 0.55),
             arrowprops=dict(facecolor='red', shrink=0.05),fontsize = 9, color='red'
             )
plt.xlabel('Time (hr)', fontsize=10)
plt.axis([0, 1.75, 0, 1.05])

plt.subplots_adjust(left=0, bottom=0 , right=1, top=2, wspace=0.1, hspace=0.25)
plt.savefig('all_activities_plot_cum.pdf', bbox_inches='tight')



