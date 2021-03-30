import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-log',
  templateUrl: './log.component.html',
  styleUrls: ['./log.component.scss']
})
export class LogComponent implements OnInit {
  isCollapsed = true;
  focus;
  focus1;
  focus2;
  username;
  pass;
  new;
  constructor(private http: HttpClient, private router: Router) { }

  ngOnInit() {
    var body = document.getElementsByTagName("body")[0];
    body.classList.add("profile-page");
  }
  ngOnDestroy() {
    var body = document.getElementsByTagName("body")[0];
    body.classList.remove("profile-page");
  }
  submitu() {
    console.log(this.username, this.pass);
    var body = new FormData()
    body.append('username', this.username)
    body.append('password', this.pass)

    this.http.post<any>("http://127.0.0.1:8000/portal/api-token-auth/", body).subscribe(
      data => {
        console.log(data)

        if (data['new'] == true) {

          localStorage.setItem('cp_token', data["token"]);
          this.router.navigateByUrl('/manager')
        }
        else if (data['new'] == false) {
          localStorage.setItem('cp_token', data["token"]);
          this.router.navigateByUrl('/candidate')
        }

      }
    )
  }
  // submit() {
  //   console.log(this.username, this.pass);
  //   var body = new FormData()
  //   body.append('username', this.username)
  //   body.append('password', this.pass)

  //   this.http.post<any>("http://127.0.0.1:8000/portal/api-token-auth/", body).subscribe(
  //     data => {
  //       console.log(data)
  //       localStorage.setItem('cp_token', data["token"])
  //       this.router.navigateByUrl('/manager')
  //     }
  //   )
  // }
}
