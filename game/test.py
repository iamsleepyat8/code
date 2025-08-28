import time
import sys

class Cursor:
    """光标控制类"""
    
    # 基本光标移动
    UP = '\033[{}A'    # 上移 n 行
    DOWN = '\033[{}B'  # 下移 n 行
    RIGHT = '\033[{}C' # 右移 n 列
    LEFT = '\033[{}D'  # 左移 n 列
    
    # 光标定位
    POSITION = '\033[{};{}H'  # 移动到指定行列 (行, 列)
    
    # 其他控制
    SAVE = '\033[s'     # 保存光标位置
    RESTORE = '\033[u'  # 恢复光标位置
    HIDE = '\033[?25l'  # 隐藏光标
    SHOW = '\033[?25h'  # 显示光标
    CLEAR_LINE = '\033[2K'  # 清除当前行
    CLEAR_SCREEN = '\033[2J'  # 清除屏幕
    
    @staticmethod
    def move_up(n=1):
        """向上移动光标 n 行"""
        print(Cursor.UP.format(n), end='')
        sys.stdout.flush()
    
    @staticmethod
    def move_down(n=1):
        """向下移动光标 n 行"""
        print(Cursor.DOWN.format(n), end='')
        sys.stdout.flush()
    
    @staticmethod
    def move_right(n=1):
        """向右移动光标 n 列"""
        print(Cursor.RIGHT.format(n), end='')
        sys.stdout.flush()
    
    @staticmethod
    def move_left(n=1):
        """向左移动光标 n 列"""
        print(Cursor.LEFT.format(n), end='')
        sys.stdout.flush()
    
    @staticmethod
    def set_position(row=1, col=1):
        """设置光标位置 (行, 列)"""
        print(Cursor.POSITION.format(row, col), end='')
        sys.stdout.flush()
    
    @staticmethod
    def save_position():
        """保存当前光标位置"""
        print(Cursor.SAVE, end='')
        sys.stdout.flush()
    
    @staticmethod
    def restore_position():
        """恢复之前保存的光标位置"""
        print(Cursor.RESTORE, end='')
        sys.stdout.flush()
    
    @staticmethod
    def hide():
        """隐藏光标"""
        print(Cursor.HIDE, end='')
        sys.stdout.flush()
    
    @staticmethod
    def show():
        """显示光标"""
        print(Cursor.SHOW, end='')
        sys.stdout.flush()
    
    @staticmethod
    def clear_line():
        """清除当前行"""
        print(Cursor.CLEAR_LINE, end='')
        sys.stdout.flush()
    
    @staticmethod
    def clear_screen():
        """清除整个屏幕"""
        print(Cursor.CLEAR_SCREEN, end='')
        sys.stdout.flush()

# 使用示例
def demo_cursor_control():
    """演示光标控制功能"""
    
    # 清除屏幕并隐藏光标
    Cursor.clear_screen()
    Cursor.hide()
    
    # 移动到屏幕顶部
    Cursor.set_position(1, 1)
    print("光标控制演示")
    
    # 向下移动两行
    Cursor.move_down(2)
    print("这是第二行")
    
    # 保存当前位置
    Cursor.save_position()
    
    # 向右移动10列
    Cursor.move_right(10)
    print("向右移动后的位置")
    
    # 恢复之前保存的位置
    Cursor.restore_position()
    Cursor.move_down(1)
    print("恢复位置后向下移动一行")
    
    # 创建一个简单的进度动画
    Cursor.set_position(10, 1)
    print("进度: [          ] 0%")
    
    for i in range(1, 11):
        # 移动到进度条位置
        Cursor.set_position(10, 9)
        
        # 更新进度条
        progress = "=" * i + " " * (10 - i)
        percent = i * 10
        print(f"[{progress}] {percent}%")
        
        time.sleep(0.5)
    
    # 显示光标
    Cursor.show()
    
    # 在底部显示完成消息
    Cursor.set_position(15, 1)
    print("演示完成!")

def simple_loading_animation():
    """简单的加载动画示例"""
    Cursor.hide()
    
    frames = ["-", "\\", "|", "/"]
    message = "处理中"
    
    for i in range(20):
        # 移动到固定位置
        Cursor.set_position(1, 1)
        Cursor.clear_line()
        
        # 显示动画帧和消息
        frame = frames[i % len(frames)]
        print(f"{message} {frame} ({i+1}/20)")
        
        time.sleep(0.1)
    
    Cursor.clear_line()
    print("处理完成!")
    Cursor.show()

if __name__ == "__main__":
    # 运行演示
    demo_cursor_control()
    
    # 等待一下
    time.sleep(2)
    
    # 清除屏幕并运行加载动画
    Cursor.clear_screen()
    simple_loading_animation()