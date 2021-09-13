import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient, HttpHeaders} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class CommonService {

  header = new HttpHeaders({'Content-Type': 'application/json'});
  constructor(private http: HttpClient) { }

  onBoardDetails():Observable<any>{
    return this.http.get('/profile/details/',{headers:this.header})
  }
  saveDetails(data:any):Observable<any>{
    return this.http.post('/getstarted/',data)
  }
}
