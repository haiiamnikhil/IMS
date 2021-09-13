import { Component, OnInit } from '@angular/core';
import { Title } from '@angular/platform-browser';
import { UserService } from 'src/app/services/user/user.service';

@Component({
  selector: 'app-listuser',
  templateUrl: './listuser.component.html',
  styleUrls: ['./listuser.component.css']
})
export class ListuserComponent implements OnInit {

  userList = []
  constructor(private user:UserService, private title:Title) { }

  ngOnInit(){
    this.user.listUsers().subscribe(response => {
      if (response.success){
        this.userList.push(response.data)
        this.title.setTitle('List User')
      } else {
        console.log("some error occured")
      }
    }, err => console.log(err))
  }

}
