import random

class Question:
    def __init__(self, prompt, options, answers):
        self.prompt = prompt
        self.options = options
        self.answers = answers if isinstance(answers, list) else [answers]

def ask_question(question):
    print(question.prompt)
    for i, option in enumerate(question.options):
        print(f"{i+1}. {option}")
    while True:
        try:
            user_answers = input("Enter your answers (comma-separated for multiple answers): ")
            user_answers = [int(ans.strip()) for ans in user_answers.split(",")]
            if all(1 <= ans <= 5 for ans in user_answers):
                break
            else:
                print("Invalid input. Please enter numbers between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter numbers.")
    return set(user_answers) == set(question.answers)

def play_quiz(questions):
    random.shuffle(questions)
    score = 0
    for question in questions:
        if ask_question(question):
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The answer was {question.answers}.\n")
    print(f"You got {score} out of {len(questions)} questions right!")

questions = [
    Question("An administrator needs to run a mixed Exchange and SQL workload with a guaranteed amount of container space for each application. How should the administrator meet this requirement?", ["Create one container and set capacity reservation ", "Create two containers and reserve space for containers ", "Create one container and enable compression ", "Create two containers and reserve space for vDisks "], 4),
    Question("A configuration is single domain, single forest, and does not use SSL. Which port number should be used to configure LDAP?", ["389", "3269", "636", "3268"], 1),   
    Question("Which best practice should be followed when creating a bond in a Nutanix cluster?", ["Place NICs of different speeds within the same bond ", "Configure the bond to use LACP ", "Only utilize NICs of the same speed within the same bond ", "Use the default bond configuration after installation "], 2),
    Question("A customer wants to isolate a group of VMs within their Nutanix environment for security reasons. The customer creates a VM with two NICs to act as a firewall and installs the appropriate software and certificates. However, no one from the outside can access the application. What is the likely cause of this problem?", ["A shared volume group must be used by all isolated VMs ", "More than one NIC cannot be added to a VM ", "One of the NICs needs to be configured on the internal VLAN ", "Wireshark is installed on the NAT VM "], 3),
    Question("What are two minimum prerequisites for live migration to succeed? Choose two.", ["All AHV hosts have IP addresses in the same subnet ", "All AHV hosts must be configured on the same VLAN ", "All VMs have an IP address in the same subnet", "All VMs are configured for the same VLAN "], [2,3]),
    Question("How should an administrator enable secure access to Volumes using a password?", ["iSER", "SAML", "CHAP", "LDAP" ], 3),
    Question("An administrator is working on a one-node ROBO cluster configuration. Which statement is true for this configuration?", ["CVM should be assigned 8 vCPUs and 20 GB memory ", "Supported hardware is NX-1175S-G5 and NX-1175S-G6 ", " C. The minimum RPO for this from factor is 8 hours ", "A Witness VM is required to break the quorum "], 2),
    Question("An administrator receives an alert email that indicates that a health check has failed. Which action should the administrator take to collect more information on the failed check?", ["In the Prism Web Console, select the URL included in the check details","Re-run the check from the CVM CLI using the ncc command ", "Forward the alert email to Nutanix Support requesting more information ", "Use the ncli command on the CVM to view the details of the check " ], 2),
    Question("A cluster has RF2. The cluster loses two drives on different nodes in the same storage tier. What is the effect on the replicas of the VMs?", ["Some VM data may be lost ", "No VMs lose data if the node has two or more SSDs ", "Some VMs may reboot and gain access to data ", "No VMs lose data because of RF2 "], 2),
    Question("An administrator needs to boot a VM to a bootable CD. The administrator tries to configure the VM to boot to it, selects to add disk, and goes to the images available. The image for the bootable CD is unavailable. What is the likely issue?", ["The CD-ROM interface is too slow ", "The bootable CD image is corrupted during creation ", "The VM needs to have a standard disk attached before it can boot to a CD ", "The administrator selected a disk instead of an ISO when creating the image " ], 2),
    Question("Which three cluster operations require an administrator to reclaim licenses? (Choose three.)", ["Upgrade a cluster ", "Migrate a cluster ", "Destroy a cluster", "Move Nodes between clusters ", "Remove a Node from a cluster "], [3, 4, 5]),
    Question("Dashboard shows VLAN 0, Power State On, 1 VM, VLAN unassigned, One Host, One switchm Unknown switch, Data Unavailable, port eth1, speed 10g, link status not connected \n An administrator logs in to Prism Element, goes to the Network view, and sees the output shown in the exhibit. Which three steps must the administrator take to increase throughput to the host? (Choose three.)", ["Change the VLAN ID to a higher priority ID", "Connect the 10Gb interfaces to the physical switch ", "Remove any 1Gb interfaces still connected from the default bond ", "Change the bond mode to balance-slb or balance-tcp ", "Add a new switch to the network and connect 1Gb interfaces to it "], [ 1, 2, 4]),
    Question("In a default configuration of an AHV cluster, a single node fails. What happens to the running VMs on that node?", ["The cluster restarts all VMs in the event of a host failure ", "The VMs do a live migration to the master node in the cluster ", "The VMs do a live migration to any other node in the cluster ", "The cluster attempts to restart VMs on other hosts "], 1),
    Question("An administrator is configuring data protection and DR for a multi-tier application. All VMs must be protected at the same time. What must the administrator do to meet this requirement?", ["Create a consistency group for each VM with identical schedules ", "Create a consistency group for the application and place all VMs in it ", "Create a protection domain for the application and select auto-protect related entities ", "Create a protection domain for each VM with identical schedules "], 2),
    Question("A two-node ROBO cluster is configured with a witness VM. What happens when Node A goes down?", ["All operations and services on the Node B are shut down and go into a waiting state ", "The cluster is unaffected and no administrator intervention is required ", "The cluster becomes unavailable and goes into read-only mode "], 2),
    Question("CPU utilization climbs above 90percent several VMs. This causes performance degradation for a business-critical application. How can alerts be configured to notify the administrator before VM CPU utilization hits 90%?", ["On the Health dashboard, locate the VM CPU Check and lower the alert threshold below 90%. ", "On a CVM, use ncli to set the VM CPU Check threshold for the critical VMs to a value below 90%. ", "On the Alerts dashboard, ensure that the VM CPU usage alert is not set to auto-resolve. ", "On a CVM, configure a cron job to run the VM CPU Check more frequently and email the result. "], 3),
    Question("When host affinity policies are enabled, how does this affect AHV cluster?", ["Microsegmentation rules will not be applied to VMs with affinity policies set on them ", "Host affinity rules do not affect any other aspects of the AHV cluster ", "Metro Availability will no longer work as designed and will result in Split Brain ", "The VM-host affinity cannot be applied on a cluster that has HA reservations configured "], 2),
    Question("An administrator has an existing Nutanix cluster that is configured to protect VMs using Time Stream. The administrator now needs to add support for protecting these VMs in AWS. Which two changes must be made to the cluster to meet this requirement? (Choose two.)", ["Configure protection domains with a 15-minute schedule ", "Add the remote site to the existing protection domains ", "Deploy a remote site for another cluster ", "Configure a remote site "], [2.3]),



]

play_quiz(questions)