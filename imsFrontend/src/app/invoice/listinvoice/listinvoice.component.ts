import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-listinvoice',
  templateUrl: './listinvoice.component.html',
  styleUrls: ['./listinvoice.component.css']
})
export class ListinvoiceComponent implements OnInit {
  invoiceDetails = [{invoiceNumber:'MEM-2021-JHJ', total : 2022, date:new Date().getDate}]
  constructor() { }

  ngOnInit(): void {
    console.log(typeof(this.invoiceDetails))
  }

}
