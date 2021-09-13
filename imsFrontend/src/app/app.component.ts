import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  page_name:String
  constructor(public router: Router){}
  
  ngOnInit(){
    this.page_name = document.title
  }
}
