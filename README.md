When I first started looking at the dataset, I honestly really didn't know what patterns to look for. My plan was to
start with basic exploratory analysis and learn the structure of the dataset. Then, I began by looking at the
most and least popular routes, which then prompted me to create some visualizations to better understand any distributions. It
was also here where I discovered the 1989 pilots strike in Australia, which I'm very grateful I looked into and didn't ignore this
event as it clears up a lot of confusion I had. Figuring out how to handle it was a bit tricky though. Eventually I decided that training/testing on clean data
and then attempting  to predict both normal periods and post-strike recovery was the most useful approach to assess my models' accuracy.
The geographic analysis was probably my strongest area. Creating the port distribution breakdown and realizing that just three southeastern ports handled 84.8% of traffic
was a significant insight I made. During this step I was also unsure of how to acquire coordinates of the Australian ports and also of destination ports
for the distance vs passenger traffic modeling. I was originally going to my own research and create a large dictionary of them to store, but I realized that Python
has a library for this. I think I could still make the calculations a bit faster though with some form of cacheing previously stored destinations. Looking past that,
this visualization made the business recommendations really clear for me. I also believe building the getPortsData() function and overall model structure
to be scalable was something I'm proud of. Initially I was just going to hardcode a few pairs, but making it work for any route combination means AeroConnect could
actually use this for their entire network. Upon looking at the distribution of the dataset, I originally considered simple linear regression and moving averages,
but quickly realized this aviation data is way more complex. The seasonal patterns were too strong to ignore, and the growth trends meant I needed something more complex than basic models.
Upon doing some research I found SARIMA modeling seemed like a straightforward match to this situation. I had to read a lot about it online and had to
play around with the parameters until I got something I was satisfied with. My final SARIMA(1,1,1)(1,1,1,12) model performed better than more complex versions I tried.
Overall, building the model to handle any route combination and any date range made it way more useful than a single-purpose Sydney-London predictor.
The model works great for normal conditions but can't necessarily predict strikes or pandemics. If I started over, I'd probably spend more time on cross-validation with
different routes to make sure my model generalizes well. I'd also want to test more parameter combinations systematically rather than just trial and error. Finally,
I would like to have looked more into the unpopular routes and see if I could essentially ignore those from this dataset as they may be
routes with just sparse data that are generally irrelevant to this study.


I also never created a separate file for storing my data, and just created or ignored
any rows/columns that were unnecessary at any point in this project.

