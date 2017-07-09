import os
import requests
import time
from nssrc.com.citrix.netscaler.nitro.service.nitro_service import nitro_service
from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception
from nssrc.com.citrix.netscaler.nitro.resource.config.ns.nsip import nsip
from nssrc.com.citrix.netscaler.nitro.resource.config.ns.nshostname import nshostname
from nssrc.com.citrix.netscaler.nitro.resource.config.dns.dnsnameserver import dnsnameserver
from nssrc.com.citrix.netscaler.nitro.resource.config.ns.nsconfig import nsconfig
from nssrc.com.citrix.netscaler.nitro.resource.config.system.systemfile import systemfile
from nssrc.com.citrix.netscaler.nitro.resource.config.basic.service import service
from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbvserver import lbvserver
from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbvserver_service_binding import lbvserver_service_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.cs.csvserver import csvserver
from nssrc.com.citrix.netscaler.nitro.resource.config.ha.hanode import hanode
from nssrc.com.citrix.netscaler.nitro.resource.config.ssl.sslcertkey import sslcertkey
from nssrc.com.citrix.netscaler.nitro.resource.config.ssl.sslcertkey_sslvserver_binding import sslcertkey_sslvserver_binding

class netscaler:
    """This class reperesents a connection to a NetScaler using NITRO. Class
    Methods below provide functionality to interact with the NetScaler."""
    
    def __init__(self):
        #initlization
        
        
        self.ns_session = ""

        self.nsip = os.environ['NSIP']
        self.username = os.environ['USERNAME']
        self.password = os.environ['PASSWORD']
        self.hostname = os.environ['HOSTNAME']
        
        self.vip1 = os.environ['VIP1']
        self.vip2 = os.environ['VIP2']
        self.vip3 = os.environ['VIP3']
        
        self.vserver1 = os.environ['VSERVER']
        self.vserver2 = os.environ['VSERVER1']
        self.vserver3 = os.environ['VSERVER2']
        
        self.service1 = os.environ['SERVICE1'] #HTTP

        self.ip = os.environ['DOCKERHOST']

        self.dns = os.environ['DNS']

    def initConnection(self):
        """Create the NetScaler session using HTTP, passing in the credentials
        to the NSIP"""
        try:
            self.ns_session = nitro_service(self.nsip,"HTTP")

            self.ns_session.set_credential(self.username, self.password)
            self.ns_session.timeout = 300

            self.ns_session.login()

        except nitro_exception as e:
            print("Exception::errorcode=" +
                  str(e.errorcode) + ",message=" + e.message)
        except Exception as e:
            print("Exception::message=" + str(e.args))

        return

    def savec(self):
        """Simple class used to save the config of the NS"""
        try:
            self.ns_session.save_config()

        except nitro_exception as e:
            print("Exception::errorcode=" +
                  str(e.errorcode) + ",message=" + e.message)
        except Exception as e:
            print("Exception::message=" + str(e.args))

        return

    def closeConnection(self, savec=False):
        """Close the session.  Can pass in if you wish to save the config or
        not.  Defaults to not saving the config"""
        try:
            if savec:
                self.savec()

            self.ns_session.logout()

        except nitro_exception as e:
            print("Exception::errorcode=" +
                  str(e.errorcode) + ",message=" + e.message)
        except Exception as e:
            print("Exception::message=" + str(e.args))

        return

    def reboot(self, wait=False, savec=False):
        """Reboot the NetScaler.  Can pass in if you wish to save the config or
        not.  Defaults to not saving the config.  You can also choose to wait
        in this function until the netscaler is back up using wait, doing so
        will re-init the connection through nitro"""
        try:
            if savec:
                self.savec()

            self.ns_session.reboot(False)

        except nitro_exception as e:
            print("Exception::errorcode=" +
                  str(e.errorcode) + ",message=" + e.message)
        except Exception as e:
            print("Exception::message=" + str(e.args))

        if wait:
            # if we want to wait lets keep checking the nitro status page for a
            # 200 OK.  If we get the 200, lets reinit the connection and cont.
            while True:
                time.sleep(15)
                try:
                    r = requests.get("http://" + self.nsip +
                                     "/nitro/v1/stat", timeout=15,
                                     auth=(self.username,
                                           self.password))
                    if r.status_code == 200:
                        # if were good to go, lets re-init that connection
                        self.initConnection()
                        break

                except requests.exceptions.Timeout as e:
                    print "TO::Waiting on", self.cfg['config']['hostname'], "to reboot..."
                except requests.exceptions.ConnectionError as e:
                    print "CE::Waiting on", self.cfg['config']['hostname'], "to reboot..."
        return

    def hostNameDnsTz(self):
        """Configure the HostName, DNS, and Time Zone for the NetScaler."""
        # Begin by setting the hostname
        try:
            newNsHostname = nshostname()
            newNsHostname.hostname = self.hostname
            nshostname.update(self.ns_session, newNsHostname)

        except nitro_exception as e:
            print("Exception::errorcode=" +
                  str(e.errorcode) + ",message=" + e.message)
        except Exception as e:
            print("Exception::message=" + str(e.args))

        # Add DNS Entries, traverse the dns class variable and add the
        # nameservers
        try:
            newDNS = dnsnameserver()
            newDNS.ip = self.dns
            dnsnameserver.add(self.ns_session, newDNS)
            
        except nitro_exception as e:
            print("Exception::errorcode=" +
                  str(e.errorcode) + ",message=" + e.message)
        except Exception as e:
            print("Exception::message=" + str(e.args))
            

        # Configure the NetScaler TimeZone
        try:
            nsconf = nsconfig()
            nsconf.timezone = "GMT-04:00-EDT-America/New_York"
            nsconfig.update(self.ns_session, nsconf)

        except nitro_exception as e:
            print("Exception::errorcode=" +
                  str(e.errorcode) + ",message=" + e.message)
        except Exception as e:
            print("Exception::message=" + str(e.args))

        return

    def confFeatures(self):
        """Configure the features for the NetScaler"""

        try:
            self.ns_session.enable_features("lb")
            self.ns_session.enable_features("ssl")
            self.ns_session.enable_features("cs")
            self.ns_session.enable_features("appfw")
        except nitro_exception as e:
            print("Exception::errorcode=" +
                  str(e.errorcode) + ",message=" + e.message)
        except Exception as e:
            print("Exception::message=" + str(e.args))

        return

    def confModes(self):
        """Configure the modes for the NetScaler"""

        try:
            self.ns_session.enable_modes("usnip")
            self.ns_session.enable_modes("l3")
            
        except nitro_exception as e:
            print("Exception::errorcode=" +
                  str(e.errorcode) + ",message=" + e.message)
        except Exception as e:
            print("Exception::message=" + str(e.args))

        return

    def addServices(self):
        """Configure the services for the NetScaler"""
        try:

            #Setup the new service 1 HTTPS
            newSVC = service()
            newSVC.name = self.service1
            newSVC.ip = self.ip
            newSVC.port = "80"
            newSVC.servicetype = "http"
            #Add the new service1 and service
            service.add(self.ns_session, newSVC)

        except nitro_exception as e:
            print("Exception::errorcode=" +
                  str(e.errorcode) + ",message=" + e.message)
        except Exception as e:
            print("Exception::message=" + str(e.args))
        return

    def addLBVServers(self):
        """Configure the lbvservers for the NetScaler"""
        #Setup a new lbvserver1
        newLBVS = lbvserver()
        newLBVS.name = self.vserver1
        newLBVS.servicetype = "ssl"
        newLBVS.ipv46 = self.vip1
        newLBVS.port = "443"
        newLBVS.persistencetype = "COOKIEINSERT"
        newLBVS.lbmethod = "ROUNDROBIN"
        
        try:
            #Add the lbvs
            response = lbvserver.add(self.ns_session, newLBVS)
            if response.severity and response.severity == "WARNING":
                print("\tWarning : " + response.message)

        except nitro_exception as e:
            print("Exception::errorcode=" +
                  str(e.errorcode) + ",message=" + e.message)
        except Exception as e:
            print("Exception::message=" + str(e.args))

        newSVCBinding = lbvserver_service_binding()
        newSVCBinding.name = self.vserver1
        newSVCBinding.servicename = self.service1
        #newSVCBinding.weight = "1"
        #Add the binding!
        try:
            lbvserver_service_binding.add(self.ns_session,
                                          newSVCBinding)
        except nitro_exception as e:
            print("Exception::errorcode=" +
                  str(e.errorcode) + ",message=" + e.message)
        except Exception as e:
            print("Exception::message=" + str(e.args))


        #Setup a new lbvserver2
        newLBVS = lbvserver()
        newLBVS.name = self.vserver2
        newLBVS.servicetype = "http"
        newLBVS.ipv46 = self.vip2
        newLBVS.port = "80"
        newLBVS.persistencetype = "COOKIEINSERT"
        newLBVS.lbmethod = "ROUNDROBIN"
        
        try:
            #Add the lbvs
            response = lbvserver.add(self.ns_session, newLBVS)
            if response.severity and response.severity == "WARNING":
                print("\tWarning : " + response.message)

        except nitro_exception as e:
            print("Exception::errorcode=" +
                  str(e.errorcode) + ",message=" + e.message)
        except Exception as e:
            print("Exception::message=" + str(e.args))

        newSVCBinding = lbvserver_service_binding()
        newSVCBinding.name = self.vserver2
        newSVCBinding.servicename = self.service1
        #newSVCBinding.weight = "1"
        #Add the binding!
        try:
            lbvserver_service_binding.add(self.ns_session,
                                          newSVCBinding)
        except nitro_exception as e:
            print("Exception::errorcode=" +
                  str(e.errorcode) + ",message=" + e.message)
        except Exception as e:
            print("Exception::message=" + str(e.args))


        #Setup a new lbvserver3
        newLBVS = lbvserver()
        newLBVS.name = self.vserver3
        newLBVS.servicetype = "http"
        newLBVS.ipv46 = self.vip3
        newLBVS.port = "80"
        newLBVS.persistencetype = "COOKIEINSERT"
        newLBVS.lbmethod = "ROUNDROBIN"
        
        try:
            #Add the lbvs
            response = lbvserver.add(self.ns_session, newLBVS)
            if response.severity and response.severity == "WARNING":
                print("\tWarning : " + response.message)

        except nitro_exception as e:
            print("Exception::errorcode=" +
                  str(e.errorcode) + ",message=" + e.message)
        except Exception as e:
            print("Exception::message=" + str(e.args))

        newSVCBinding = lbvserver_service_binding()
        newSVCBinding.name = self.vserver3
        newSVCBinding.servicename = self.service1
        #newSVCBinding.weight = "1"
        #Add the binding!
        try:
            lbvserver_service_binding.add(self.ns_session,
                                          newSVCBinding)
        except nitro_exception as e:
            print("Exception::errorcode=" +
                  str(e.errorcode) + ",message=" + e.message)
        except Exception as e:
            print("Exception::message=" + str(e.args))

        return
    
    def addcerts(self):

        certs = { "512" : ["sha1", "sha224", "sha256"], "4096" : ["sha1", "sha224", "sha256", "sha384", "sha512"], "2048" : ["sha1", "sha224", "sha256", "sha384", "sha512"], "1024" : ["sha1", "sha224", "sha256", "sha384", "sha512"] }

        for cert in certs : 
            for sha in certs[cert] :
                cert_name = "root_rsa_" + cert + "_" + sha + ".pem" 
                print(cert_name)
                key_name = "root_rsa_" + cert + "_" + sha + ".ky" 
                print(key_name)
                
                newcert = sslcertkey()
                newcert.certkey = cert + "_" + sha
                newcert.cert = cert_name
                newcert.key = key_name
                
                try:
                    sslcertkey.add(self.ns_session,newcert)

                except nitro_exception as e:
                    print("Exception::errorcode=" +
                          str(e.errorcode) + ",message=" + e.message)
                except Exception as e:
                    print("Exception::message=" + str(e.args))
        return
    

if __name__ == '__main__':
    """ This is our main thread of execution, it starts all the work!"""
    '''
    # read in cnfig http://www.objgen.com/json/models/mdui
    # fin = open("nsAutoCfg.json", "r")
    # json_raw = fin.read()
    # fin.close()
    # jsn = json.loads(json_raw)

    # Create some threads and netscalers 
    '''
    ns = netscaler()
    ns.initConnection()
    # ns.defineIPs()
    ns.hostNameDnsTz()
    # ns.uploadLicense()
    # ns.reboot(True, True)
    ns.confFeatures()
    ns.confModes()

    # Lets add the certificates to the NS
    ns.addcerts()

    # Next lets add services and configure VServers
    ns.addServices()
    ns.addLBVServers()

    # Were done here, lets save and close the connection
    ns.savec()
    ns.closeConnection()
    print "All done preforming configuration"

