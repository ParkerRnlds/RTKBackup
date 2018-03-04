object GoogleMapView: TGoogleMapView
  Left = 0
  Top = 0
  BorderIcons = [biSystemMenu, biMaximize]
  Caption = 'Google Map View'
  ClientHeight = 662
  ClientWidth = 1030
  Color = clBtnFace
  Constraints.MinHeight = 240
  Constraints.MinWidth = 424
  DoubleBuffered = True
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'Tahoma'
  Font.Style = []
  OldCreateOrder = False
  OnCreate = FormCreate
  PixelsPerInch = 96
  TextHeight = 13
  object Panel1: TPanel
    Left = 0
    Top = 0
    Width = 1030
    Height = 22
    Align = alTop
    TabOrder = 0
    object BtnHome: TSpeedButton
      Left = 1
      Top = 0
      Width = 23
      Height = 22
      Flat = True
      Glyph.Data = {
        06050000424D060500000000000036040000280000000D0000000D0000000100
        080000000000D000000000000000000000000001000000000000000000000000
        80000080000000808000800000008000800080800000C0C0C000C0DCC000F0CA
        A6000020400000206000002080000020A0000020C0000020E000004000000040
        20000040400000406000004080000040A0000040C0000040E000006000000060
        20000060400000606000006080000060A0000060C0000060E000008000000080
        20000080400000806000008080000080A0000080C0000080E00000A0000000A0
        200000A0400000A0600000A0800000A0A00000A0C00000A0E00000C0000000C0
        200000C0400000C0600000C0800000C0A00000C0C00000C0E00000E0000000E0
        200000E0400000E0600000E0800000E0A00000E0C00000E0E000400000004000
        20004000400040006000400080004000A0004000C0004000E000402000004020
        20004020400040206000402080004020A0004020C0004020E000404000004040
        20004040400040406000404080004040A0004040C0004040E000406000004060
        20004060400040606000406080004060A0004060C0004060E000408000004080
        20004080400040806000408080004080A0004080C0004080E00040A0000040A0
        200040A0400040A0600040A0800040A0A00040A0C00040A0E00040C0000040C0
        200040C0400040C0600040C0800040C0A00040C0C00040C0E00040E0000040E0
        200040E0400040E0600040E0800040E0A00040E0C00040E0E000800000008000
        20008000400080006000800080008000A0008000C0008000E000802000008020
        20008020400080206000802080008020A0008020C0008020E000804000008040
        20008040400080406000804080008040A0008040C0008040E000806000008060
        20008060400080606000806080008060A0008060C0008060E000808000008080
        20008080400080806000808080008080A0008080C0008080E00080A0000080A0
        200080A0400080A0600080A0800080A0A00080A0C00080A0E00080C0000080C0
        200080C0400080C0600080C0800080C0A00080C0C00080C0E00080E0000080E0
        200080E0400080E0600080E0800080E0A00080E0C00080E0E000C0000000C000
        2000C0004000C0006000C0008000C000A000C000C000C000E000C0200000C020
        2000C0204000C0206000C0208000C020A000C020C000C020E000C0400000C040
        2000C0404000C0406000C0408000C040A000C040C000C040E000C0600000C060
        2000C0604000C0606000C0608000C060A000C060C000C060E000C0800000C080
        2000C0804000C0806000C0808000C080A000C080C000C080E000C0A00000C0A0
        2000C0A04000C0A06000C0A08000C0A0A000C0A0C000C0A0E000C0C00000C0C0
        2000C0C04000C0C06000C0C08000C0C0A000F0FBFF00A4A0A000808080000000
        FF0000FF000000FFFF00FF000000FF00FF00FFFF0000FFFFFF00FFFFFFFFFFFF
        FFFFFFFFFFFFFF000000FFFFFFFFFFFFFFFFFFFFFFFFFF000000FFFFFF000000
        00000000FFFFFF000000FFFFFF00FFFFFFFFFF00FFFFFF000000FFFFFF00FFFF
        FFFFFF00FFFFFF000000FFFFFF00FFFFFFFFFF00FFFFFF000000FF000000FFFF
        FFFFFF000000FF000000FF0700FFFFFFFFFFFFFF0007FF000000FFFF0700FFFF
        FFFFFF0007FFFF000000FFFFFF0700FFFFFF0007FFFFFF000000FFFFFFFF0700
        FF0007FFFFFFFF000000FFFFFFFFFF070007FFFFFFFFFF000000FFFFFFFFFFFF
        FFFFFFFFFFFFFF000000}
      OnClick = BtnHomeClick
    end
    object Panel5: TPanel
      Left = 978
      Top = 1
      Width = 51
      Height = 20
      Align = alRight
      BevelOuter = bvNone
      Caption = 'Panel5'
      TabOrder = 0
      object BtnClose: TButton
        Left = 0
        Top = 0
        Width = 51
        Height = 20
        Align = alClient
        Caption = 'Close'
        TabOrder = 0
        OnClick = BtnCloseClick
      end
    end
  end
  object Panel2: TPanel
    Left = 0
    Top = 22
    Width = 1030
    Height = 640
    Align = alClient
    Caption = 'Panel2'
    TabOrder = 1
    ExplicitHeight = 748
    object WebBrowser: TCppWebBrowser
      Left = 1
      Top = 1
      Width = 1028
      Height = 638
      Align = alClient
      TabOrder = 0
      ExplicitTop = 0
      ExplicitWidth = 502
      ExplicitHeight = 482
      ControlData = {
        4C0000003F6A0000F04100000000000000000000000000000000000000000000
        000000004C000000000000000000000001000000E0D057007335CF11AE690800
        2B2E12620B000000000000004C0000000114020000000000C000000000000046
        8000000000000000000000000000000000000000000000000000000000000000
        00000000000000000100000000000000000000000000000000000000}
    end
  end
end
