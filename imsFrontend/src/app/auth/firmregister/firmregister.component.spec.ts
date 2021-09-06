import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FirmregisterComponent } from './firmregister.component';

describe('FirmregisterComponent', () => {
  let component: FirmregisterComponent;
  let fixture: ComponentFixture<FirmregisterComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FirmregisterComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FirmregisterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
