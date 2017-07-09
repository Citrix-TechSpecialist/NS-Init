mkdir ~/.lftp
echo "set ssl:verify-certificate false" >> ~/.lftp/rc
echo "set sftp:auto-confirm yes" >> ~/.lftp/rc
cd /scripts
lftp sftp://$USERNAME:$PASSWORD@$NSIP/nsconfig/ -e "mirror -R ./ssl/ ; quit"
