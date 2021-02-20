# raspi_relay_using_cron
This very simple project uses Cron to execute scripts in your Raspberry Pi. Literally, the easiest way to go, and using, zero resources.

*Setting up*

In my case, I set up the whole thing using Cron. It is easier, and you don’t need to complicate yourself too much with schedulers (if properly done).

The Cron is designed for these kind of tasks, scheduled tasks, scripts, etc. Where is it? /etc/crontab

However, to edit it we do not need to do much. Just write:
>> crontab -e


and add these lines here. In my case, I am using 6 and 18 everyday. This of course can be changed.
0 6 * * * python /home/pi//home/pi/test/Raspi_Projects/raspi_relay_using_cron/src/ch1_on.py
0 18 * * * python /home/pi/Raspi_Projects/raspi_relay_using_cron/src/ch1_off.py
@reboot python /home/pi/Raspi_Projects/raspi_relay_using_cron/src/ch_reboot.py


cd ~/.ssh
mkdir -p ~/.ssh
chmod 0700 ~/.ssh
cd ~/.ssh
ls -lah
ssh-keygen -t rsa -C "jperezmacias@gmail.com"
cat id_rsa.pub 

Add it to Github > Settings > keys

ssh-agent bash -c 'ssh-add ~/.ssh/id_rsa.pub; git clone git@github.com:jperezmacias/raspi_relay_using_cron.git'

