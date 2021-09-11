import { Component, OnInit } from '@angular/core';
import { UserService } from 'src/app/services/user/user.service';

@Component({
  selector: 'app-listuser',
  templateUrl: './listuser.component.html',
  styleUrls: ['./listuser.component.css']
})
export class ListuserComponent implements OnInit {

  constructor(private user: UserService) { }

  ngOnInit(){
    this.user.listUsers().subscribe(data => console.log(data),err => console.log(err));
  }

}
