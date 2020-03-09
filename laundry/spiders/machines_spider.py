import scrapy
import datetime
from scrapy.utils.response import open_in_browser

class MachineSpider(scrapy.Spider):
    name = "machines"	
    start_urls = ['http://washalert.washlaundry.com/washalertweb/calpoly/WASHALERtweb.aspx?location=007d2e0c-92c4-4a01-a0df-dcd0eb81caf0', 'http://washalert.washlaundry.com/washalertweb/calpoly/WASHALERtweb.aspx?location=239a9c27-e7ee-4a83-81e0-b3d056b8079c',]

    def parse(self, response):
        currentDT = datetime.datetime.now()
        date = currentDT.strftime("%m-%d-%Y")
        time = currentDT.strftime("%H:%M")
        possible_stats = ["tr.MachineReadyMode", "tr.MachineDoorOpenReadyMode", "tr.MachineEndOfCycleMode", "tr.MachineRunModeAlmostDone", "tr.MachineRunMode", "tr.MachineUnableToConnectToMachine"]
        for stat in possible_stats:
            for machine in response.css(stat):
                yield {
                        'date': date,
                        'time':time,
                        'number': machine.css('td.name::text').get(), 
                        'type': machine.css('td.type::text').get(),
                        'status': machine.css('td.status::text').get(),
                        'rem': machine.css('td.time::text').get(),
                         }
